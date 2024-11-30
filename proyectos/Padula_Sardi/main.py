from machine import Pin, I2C
from utime import sleep, ticks_ms, ticks_diff
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# Configuración de LEDs
leds = [Pin(2, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT)]

# Configuración del botón
boton = Pin(27, Pin.IN, Pin.PULL_UP)

# Configuración del LCD
i2c = I2C(0, scl=Pin(22), sda=Pin(23))  # Pines I2C
lcd_address = 0x27  # Dirección I2C del LCD
lcd_display = I2cLcd(i2c, lcd_address, 2, 16)

# Definir caracteres personalizados para el LCD
campana = bytearray([ 0x04,  0x04,  0x0E,  0x0E,  0x0E,  0x0E,  0x1F,  0x08,  0x00])
campana1 = bytearray([0x04,
   0x04,
  0x0E,
  0x0E,
  0x0E,
  0x0E,
  0x1F,
  0x02,
  0x00])
lcd_display.custom_char(0, campana)
lcd_display.custom_char(1, campana1)
modo_lcd=0

# Variables de control
modo_actual = 0
estado_boton_anterior = 1
ultimo_cambio = ticks_ms()
debounce_time = 200  # Tiempo de debounce en ms
paso = 0  # Paso actual dentro del modo
ultimo_paso = ticks_ms()

# Funcion 0: "Parapdeo clasico"
def modo_clasico(paso):
    if paso == 0:
        leds[0].on()
        leds[1].on()
        leds[2].on()
        leds[3].on()
        leds[4].on()
    elif paso == 1:
        leds[0].off()
        leds[1].off()
        leds[2].off()
        leds[3].off()
        leds[4].off()

# Función 1: "Estrella centelleante"
def modo_estrella(paso):
    for i in range(len(leds)):
        if i % 2 == paso % 2:
            leds[i].on()  # LEDs pares e impares alternan
        else:
            leds[i].off()

# Función 2: "Espiral luminosa"
def modo_espiral(paso):
    for i in range(len(leds)):
        leds[i].off()
    leds[paso % len(leds)].on()  # LED activo se desplaza como un efecto de espiral
    leds[(paso + 2) % len(leds)].on()  # Agrega un segundo LED encendido en otro punto

# Función 3: "Cascada"
def modo_cascada(paso):
    for i in range(len(leds)):
        leds[i].off()  # Apagar todos los LEDs
    if paso < len(leds):
        leds[len(leds) - paso - 1].on()  # Encender LEDs en orden inverso

# Función 4: "Encendido progresivo y apagado escalonado"
def modo_progresivo(paso):
    for i in range(len(leds)):
        leds[i].off()  # Apagar todos los LEDs inicialmente

    if paso == 0:  # Encender los LEDs de los extremos
        leds[0].on()
        leds[-1].on()
    elif paso == 1:  # Encender LEDs 1 y 4 (los que están al lado de los extremos)
        leds[0].on()
        leds[-1].on()
        leds[1].on()
        leds[-2].on()
    elif paso == 2:  # Encender todos los LEDs
        for led in leds:
            led.on()
    elif paso == 3:  # Apagar el LED del medio (LED 3)
        leds[0].on()
        leds[-1].on()
        leds[1].on()
        leds[-2].on()
        leds[2].off()
    elif paso == 4:  # Apagar LED 2 y LED 4
        leds[0].on()
        leds[-1].on()
        leds[1].off()
        leds[3].off()


# Función para mostrar en el LCD el modo activo
def mostrar_lcd(modo):
    if modo==0:
        lcd_display.putstr(" Feliz Navidad ")
        lcd_display.move_to(0, 1)
        campanas = [chr(0)] * 6
        lcd_display.putstr(" " + "".join(campanas).center(14) + " ")
    elif modo==1:
        lcd_display.putstr(" Feliz Navidad ")
        lcd_display.move_to(0, 1)
        campanas1 = [chr(1)] * 6
        lcd_display.putstr(" " + "".join(campanas1).center(14) + " ")




# Bucle principal
while True:
    boton_presionado = boton.value()
    ahora = ticks_ms()

    # Detectar flanco de bajada (presionado) con debounce
    if boton_presionado == 0 and estado_boton_anterior == 1 and ticks_diff(ahora, ultimo_cambio) > debounce_time:
        ultimo_cambio = ahora
        modo_actual = (modo_actual + 1) % 5  # Cambiar entre modos 0, 1, 2, 3 y 4
        paso = 0  # Reinicia el paso al cambiar de modo

    estado_boton_anterior = boton_presionado

    # Control de modos paso a paso
    if ticks_diff(ahora, ultimo_paso) > 500:  # Avanzar cada 500 ms
        if modo_actual == 0:
            modo_clasico(paso)
        elif modo_actual == 1:
            modo_estrella(paso)
        elif modo_actual == 2:
            modo_espiral(paso)
        elif modo_actual == 3:
            modo_cascada(paso)
        elif modo_actual == 4:
            modo_progresivo(paso)

        paso = (paso + 1) % (len(leds) if modo_actual != 0 else 2)
        ultimo_paso = ahora

        # Mostrar información en el LCD
        mostrar_lcd(modo_lcd)
        if modo_lcd==0:
            modo_lcd=1
        else:
            modo_lcd=0
