# Encender y apagar el led incorporado

from machine import Pin
from time import sleep_ms

# Configurar el pin GPIO 2 como salida (LED incorporado)
led = Pin(2, Pin.OUT)

# Bucle infinito para parpadear el LED
while True:
    led.value(True)
    sleep_ms(500)
    led.value(False)
    sleep_ms(1000)