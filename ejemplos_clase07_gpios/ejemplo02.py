from machine import Pin
from utime import sleep

from machine import Pin
from utime import sleep

# Configurar los pines de los leds como salidas
led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(4, Pin.OUT)
led_rojo = Pin(5, Pin.OUT)

# Configurar los pines de los leds como entradas con resistencias de pull-up
boton_verde = Pin(25, Pin.IN, Pin.PULL_UP)
boton_amarillo = Pin(26, Pin.IN, Pin.PULL_UP)
boton_rojo = Pin(27, Pin.IN, Pin.PULL_UP)

while True:
    if boton_verde.value() == 0:  # Si el botón está presionado
        led_verde.on()
        sleep(0.1)
        led_verde.off()
    if boton_amarillo.value() == 0:  # Si el botón está presionado
        led_amarillo.on()
        sleep(0.1)
        led_amarillo.off()
    if boton_rojo.value() == 0:  # Si el botón está presionado
        led_rojo.on()
        sleep(0.1)
        led_rojo.off()