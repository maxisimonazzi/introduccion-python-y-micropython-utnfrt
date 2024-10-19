# Encender y apagar el led incorporado

from machine import Pin
from time import sleep

# Configurar el pin GPIO 2 como salida (LED incorporado)
led = Pin(2, Pin.OUT)

# Bucle infinito para parpadear el LED
while True:
    led.on()  # Encender el LED
    sleep(1)  # Esperar 1 segundo
    led.off()  # Apagar el LED
    sleep(1)  # Esperar 1 segundo