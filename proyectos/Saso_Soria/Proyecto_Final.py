from machine import Pin, SoftI2C
import ssd1306
from menuoled import MENU_OPTIONS, NAVIGATE_MENU , MENU
import time
import dht
from hcsr04 import HCSR04


# Funciones menu
def plot_menu():
    print("Main Menu")
    main_menu.draw()

def show_icons_menu():
    print("Icons Menu")
    icons_menu.draw()

def show_temp_hum_menu():
    print("Clima Menu")
    clima_menu.draw()

def show_distance_menu():
    print("Distance menu")
    distancia_menu.draw()
    
#Funcion menu clima
    
def leer_temperatura():
    try:
        d.measure()  # Intentar medir el sensor
        temp = d.temperature()
        return temp
    except OSError as e:
        print(f"Error al leer el sensor de temperatura: {e}")
        return None  # En caso de error, retorna None

def leer_humedad():
    try:
        d.measure()  # Intentar medir el sensor
        hum = d.humidity()
        return hum
    except OSError as e:
        print(f"Error al leer el sensor de humedad: {e}")
        return None  # En caso de error, retorna None

def mostrar_temperatura():
    print("Mostrando Temperatura")
    temperatura = leer_temperatura()
    if temperatura is not None:
        display.fill_rect(0, 10, 128, 16, 0)
        display.text(f"{temperatura:.1f} C", 0, 10)
    else:
        display.fill_rect(0, 10, 128, 16, 0)
        display.text("Error sensor", 0, 10)
    display.show()
    time.sleep(1)

def mostrar_humedad():
    print("Mostrando Humedad")
    humedad = leer_humedad()
    if humedad is not None:
        display.fill_rect(0, 10, 128, 16, 0)
        display.text(f"{humedad:.1f} %", 0, 10)
    else:
        display.fill_rect(0, 10, 128, 16, 0)
        display.text("Error sensor", 0, 10)
    display.show()
    time.sleep(1)

# Funciones menu imagen    
def plot_pikachu():
    print("Mostrar Pikachu")
    imagen = fotos.openIcon("pickachu")
    display.fill(0)  # Limpiar la pantalla
    display.blit(imagen, 0, 0)  # Dibuja el buffer en la pantalla
    display.show()  # Actualiza la pantalla para mostrar la imagen
        
def plot_troll():
    print("Mostrar TrollFace")
    imagen = fotos.openIcon("Trollface")
    display.fill(0)  # Limpiar la pantalla
    display.blit(imagen, 0, 0)  # Dibuja el buffer en la pantalla
    display.show()  # Actualiza la pantalla para mostrar la imagen

def plot_utn():
    print("Mostrar logo UTN")
    imagen = fotos.openIcon("LOGO")
    display.fill(0)  # Limpiar la pantalla
    display.blit(imagen, 0, 0)  # Dibuja el buffer en la pantalla
    display.show()  # Actualiza la pantalla para mostrar la imagen
    
def plot_camara():
    print("Mostrar Camara")
    imagen = fotos.openIcon("insta")
    display.fill(0)  # Limpiar la pantalla
    display.blit(imagen, 0, 0)  # Dibuja el buffer en la pantalla
    display.show()  # Actualiza la pantalla para mostrar la imagen

#Funcion menu distancia
    
def distancia_cm():
    try:
        cm = medidor.distance_cm()
        return cm
    except OSError as e:
        print(f"Error al leer el sensor ultrasonico: {e}")
        return None  # En caso de error, retorna None

def distancia_mm():
    try:
        mm = medidor.distance_mm()
        return mm
    except OSError as e:
        print(f"Error al leer el sensor ultrasonico: {e}")
        return None  # En caso de error, retorna None
    
def mostrar_distancia_cm():
    print("Mostrando distancia en cm")
    time.sleep(0.3)
    while True:
        dis_cm = distancia_cm()
        display.fill_rect(0, 10, 128, 16, 0)
        if dis_cm is not None:
            display.text(f"{dis_cm:.1f} cm", 0, 10)  
        else:
            display.text("Error sensor", 0, 10)  
        display.show()
        if button_select.value():
            print("Regresando al menú anterior")
            plot_menu()
            break 
        time.sleep(0.5)
        if button_menu.value():
            buttom_plot_menu()
            time.sleep(0.5)
            break

def mostrar_distancia_mm():
    print("Mostrando distancia en mm")
    time.sleep(0.3)
    while True:
        dis_mm = distancia_mm()
        display.fill_rect(0, 10, 128, 16, 0)
        if dis_mm is not None:
            display.text(f"{dis_mm:.1f} mm", 0, 10) 
        else:
            display.text("Error sensor", 0, 10)
        display.show()
        if button_select.value():
            print("Regresando al menú anterior")
            plot_menu()
            break  
        time.sleep(0.5)
        if button_menu.value():
            buttom_plot_menu()
            time.sleep(0.5)
            break
         
# Funcion escape
def buttom_plot_menu():
    plot_menu()
    print("Main Menu")
    main_menu.draw()

# Declaración de pines
pin_up = 13
pin_down = 12
pin_select = 14
pin_menu = 27
pin_dht = 19
pin_hcsr_trigger=2
pin_hcsr_echo=4

# Configuración de I2C y el display usando SoftI2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

#Configuración de HCSR04
medidor = HCSR04 (trigger_pin=pin_hcsr_trigger , echo_pin=pin_hcsr_echo )

# Menú principal del sistema
main_menu = MENU_OPTIONS(display)

main_menu.add_option("Imagenes", show_icons_menu)
main_menu.add_option("Clima", show_temp_hum_menu)
main_menu.add_option("Distancia", show_distance_menu)


# Menú de imágenes
icons_menu = MENU_OPTIONS(display)
fotos = MENU(display)

icons_menu.add_option("Pikachu", plot_pikachu)
icons_menu.add_option("Camara", plot_camara)
icons_menu.add_option("Trollface", plot_troll)
icons_menu.add_option("UTN", plot_utn)

# Menú del clima
clima = MENU(display)
clima_menu = MENU_OPTIONS(display)

clima_menu.add_option("Temperatura",mostrar_temperatura)
clima_menu.add_option("Humedad",mostrar_humedad)

# Menú de distancia
distancia = MENU(display)

distancia_menu = MENU_OPTIONS(display)

distancia_menu.add_option("Distancia en mm", mostrar_distancia_mm)
distancia_menu.add_option("Distancia en cm", mostrar_distancia_cm)


# Configuración de los botones
button_up = Pin(pin_up, Pin.IN, Pin.PULL_DOWN)
button_down = Pin(pin_down, Pin.IN, Pin.PULL_DOWN)
button_select = Pin(pin_select, Pin.IN, Pin.PULL_DOWN)
button_menu = Pin(pin_menu, Pin.IN, Pin.PULL_DOWN)

# Configuración de sensores
d = dht.DHT11(Pin(pin_dht))


# Lista de menús para navegar
menu_list = [main_menu, icons_menu, clima_menu, distancia_menu]
menu = NAVIGATE_MENU(menu_list)

# Mostrar el menú principal
plot_menu()

# Bucle principal para manejo de botones
while True:
    if button_up.value():
        print("Arriba")
        menu.navigate("up")
        time.sleep(0.5)  # Pausa para evitar múltiples lecturas
    if button_down.value():
        print("Abajo")
        menu.navigate("down")
        time.sleep(0.5)
    if button_select.value():
        print("Seleccionar")
        menu.select()
        time.sleep(0.5)
    if button_menu.value():
        buttom_plot_menu()
        time.sleep(0.5)