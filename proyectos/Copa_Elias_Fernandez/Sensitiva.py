from machine import Pin, ADC, I2C
from time import ticks_ms, sleep as delay

from i2c_lcd import I2cLcd


# Configuración de pines
Pines= [0, 2, 4, 15, 5, 17, 16, 18, 19, 
        0, 13, 12, 14, 27, 26, 25, 33, 23, 32]

# Pines de Salida digital DO
DO = [Pin(pin, Pin.OUT) for pin in Pines[0:9]]  # Salidas digitales DO1 a DO10
Salidas= {
    "Husillo"    : DO[1], #Husillo
    "Carro"      : DO[2], #Carro
    "Inv Carro"  : DO[3], #Inversion de marcha del Carro
    "Vel rapida" : DO[4], #Velocidad rápida del Carro
    "Division"   : DO[5], #División
    "EV Up"      : DO[6], #Cilindro hacia arriba
    "EV Down"    : DO[7], #Cilindro hacia abajo
    "Fin"        : DO[8]  #Fin del ciclo
    }

# Pines de entrada digital DI
DI = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in Pines[9:19]]  # Entradas digitales DI1 a DI8
Entradas = {
    "K1"    : DI[1],  #Fin de carrera +X
    "K2"    : DI[2],  #Fin de carrera -X
    "K3"    : DI[3],  #Fin de carrera +Y
    "K4"    : DI[4],  #Fin de carrera -Y
    "PT"    : DI[5],  #Error Protección Térmica
    "PS"    : DI[6],  #Presostato
    "Start" : DI[7],  #Inicio de ciclo
    "Modo"  : DI[8],  #Perilla modo automático/manual
    "Stop"  : DI[9]   #Parada de emergencia
    }

# Pines de entrada analógica AI   
AI1 = ADC(Pin(34))  # Potenciómetro P1 (regulación bajada EVB1)
AI2 = ADC(Pin(39))  # Potenciómetro P2 (regulación división)
AI3 = ADC(Pin(36))  # Potenciómetro P3 (regulación de la cantidad de cortes)

# Configuración de ADC para rango completo (0 a 3.3V)
AI1.atten(ADC.ATTN_11DB)
AI2.atten(ADC.ATTN_11DB)
AI3.atten(ADC.ATTN_11DB)

Potenciometro = {
    "P1"    :   AI1,    # Tiempo de bajada
    "P2"    :   AI2,    # Tiempo de división
    "P3"    :   AI3     # Número de cortes
}

# Configuración de I2C para la pantalla LCD
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Interrupción para cambio de numero de cortes
set_cortes= 0

def Cortes():
    global set_cortes
    if leer("P3", 11)+1 != set_cortes:
        print(int(leer("P3", 11)))
        mostrar_mensaje("Nro de cortes:")
        mostrar_mensaje("               ", 0, 1)
        mostrar_mensaje(str(int(leer("P3",11))+1), 10, 1)
        set_cortes = leer("P3", 11)+1


#Función para determinar el tiempo transcurrido en segundos
def time():
    return ticks_ms()/1000

# Función para mostrar mensajes en pantalla
def mostrar_mensaje(mensaje, fila=0, columna=0):
    lcd.move_to(fila, columna)
    lcd.putstr(mensaje)
    
# Función para activar una salida digital
def activar(salida1, salida2=None):
    Salidas[salida1].on()
    if salida2 is not None:
        Salidas[salida2].on()
    
# Función para desactivar una salida digital
def desactivar(salida1, salida2=None):
    Salidas[salida1].off()
    if salida2 is not None:
        Salidas[salida2].off()
    
# Función para leer entrada digital
def leer(entrada, escala=None):
    if entrada in ["P1", "P2", "P3"]:
        return (Potenciometro[entrada].read()/4095)*escala
    else:
        return Entradas[entrada].value()
    
# Función para detener todas las salidas digitales
def detener_todo():
    for salida in DO:
        salida.off()


# Verificar posición inicial de K4 y K2
def verificar_posicion_inicial():
    if not leer("K2") or not leer("K4"):  # K4 y K2
        return False
    return True


# Listado de Errores
def Falla(error):
    #   Error 1: Protección Térmica
    if error == "Error 1":
        lcd.clear()
        mostrar_mensaje("Error 1:      ")
        mostrar_mensaje("Prot Termica  ",0,1)

    if error == "Error 2":
        lcd.clear()
        mostrar_mensaje("Error 2:      ")
        mostrar_mensaje("Presostato    ",0,1)

    if error == "Error 3":
        lcd.clear()
        mostrar_mensaje("Error 3:      ")
        mostrar_mensaje("Parada Emergen",0,1)

    if error == "Error 4":
        lcd.clear()
        mostrar_mensaje("Error 4: K2-K4  ")
        activar("Fin")

    if error == "Error 5":
        lcd.clear()
        mostrar_mensaje("Error 5: K1     ")
        activar("Fin")

    if error == "Error 6":
        lcd.clear()
        mostrar_mensaje("Error 6: K2     ")
        activar("Fin")

    if error == "Error 7":
        lcd.clear()
        mostrar_mensaje("Error 7: K4     ")
        activar("Fin")
    
    if error == None:
        return False
    
    delay(1)
    detener_todo()
    return True


# Secuencia automática
def Secuencia_automatica():
    #Paso 1: Verificación de posición inicial
    if not verificar_posicion_inicial():
        return "Error 4"

    # Paso 2: Acercamiento del carro rápidamente (R1, R3)
    lcd.clear()
    mostrar_mensaje("Moviendo a K1")
    activar("Carro", "Vel rapida")    # Activar carro a velocidad rápida(R1 y R3)
    inicio_tiempo = time()  # Inicia tiempo de espera
    while not leer("K1"):  # Espera por K1
        if time() - inicio_tiempo > 15:  # Timeout de 5 segundos
            activar("Fin")
            delay(1)
            return "Error 5"

    desactivar("Carro", "Vel rapida")  # Detener R1 y R3

    # Paso 3: Bajar herramienta (EVB2)
    lcd.clear()
    mostrar_mensaje("Bajando herramienta")
    inicio_tiempo= time()
    activar("EV Down")  # Activar B2
    while not leer("K3"):  #Espera por K3
        tiempo_bajada = leer("P1", 5)
        if time() - inicio_tiempo > tiempo_bajada:    
            break
    desactivar("EV Down")  # Detener B2

    # Paso 4: Encender husillo
    lcd.clear()
    mostrar_mensaje("Encendiendo husillo")
    activar("Husillo")  # Activar husillo M1

    # Paso 5: Avanzar carro a velocidad controlada
    lcd.clear()
    mostrar_mensaje("Avanzando a K2")
    activar("Carro")  # Activar avance (R1)
    inicio_tiempo = time()
    while not leer("K2"):  # Espera por K2
        if time() - inicio_tiempo > 25:  # Timeout de 25 segundos
            activar("Fin")
            delay(1)
            return "Error 6"
    desactivar("Carro")  # Detener avance

    # Paso 6: Apagar husillo
    lcd.clear()
    mostrar_mensaje("Apagando husillo")
    desactivar("Husillo")

    # Paso 7: Subir herramienta (EVB2)
    lcd.clear()
    mostrar_mensaje("Subiendo herramienta")
    activar("EV Up")  # Activar bobina B1
    inicio_tiempo = time()
    while not leer("K4"):  # Espera por K4
        if time() - inicio_tiempo > 10:
            return "Error 7"
    desactivar("EV Up")  # Detener B1


    # Paso 8: Activar división
    lcd.clear()
    mostrar_mensaje("Inicio division")
    activar("Division")  # Activar división M4
    tiempo_division = leer("P2", 5)
    delay(tiempo_division)
    desactivar("Division")  # Detener M4

    # Repetir desde el paso 1
    mostrar_mensaje("Corte completado")
    delay(2)
 
# Manejo de interrupciones
def interrupciones(pin):
    detener_todo()
    while leer("PT") or leer("Stop") or leer("PS"):
        if leer("PT"):
            Falla("Error 1")
            delay(2)
        
        if leer("PS"):
            Falla("Error 2")
            delay(2)

        if leer("Stop"):
            Falla("Error 3")
            delay(2)


        lcd.clear()

# Interrupcion por PT:
DI[5].irq(trigger=Pin.IRQ_RISING, handler=interrupciones)    

# Interrupción por PS:
DI[6].irq(trigger=Pin.IRQ_RISING, handler=interrupciones)

# Interrupción por STOP:
DI[9].irq(trigger=Pin.IRQ_RISING, handler=interrupciones)    

K= [0, 0, 0, 0, 0]

def monitoreo():
    global K
    

    if leer("K1") and not K[1]:
        mostrar_mensaje("K1        ")    
    if not leer("K1") and K[1]:
        mostrar_mensaje("          ")

    if leer("K2") and not K[2]:
        mostrar_mensaje("K2   ",10,0)    
    if not leer("K2") and K[2]:
        mostrar_mensaje("     ",10,0)

    if leer("K3") and not K[3]:
        mostrar_mensaje("K3        ",0,1)    
    if not leer("K3") and K[3]:
        mostrar_mensaje("          ",0,1)

    if leer("K4") and not K[4]:
        mostrar_mensaje("K4   ",10,1)    
    if not leer("K4") and K[4]:
        mostrar_mensaje("     ",10,1)


    for i in range (1,5):
        if K[i] != DI[i].value():
            K[i]= DI[i].value() 
    


def main():
    global set_cortes
    mostrar_mensaje("Sensitiva ON")
    delay(2)
    lcd.clear()
    while True:
        if leer("Modo"):
            print("Modo Automático OK")
            Cortes()
            if leer("Start" ):
                print("Start OK")
                for i in range (set_cortes-1):
                    print("Secuencia OK. Corte: ", i+1)
                    if Falla(Secuencia_automatica()):
                        break
                mostrar_mensaje("Ciclo terminado",0,1)
                activar("Fin")
            
            else:
                print("Detenido. A la espera")
            
            detener_todo()
            delay(1)
                
        else:
            print("Modo Manual OK")
            monitoreo() 
            delay(0.1)           
        

main()