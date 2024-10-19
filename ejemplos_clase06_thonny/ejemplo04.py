# Este ejemplo hace que el LED parpadee con diferentes intervalos de tiempo.

from machine import Pin
from time import sleep

# Configurar el pin GPIO 2 como salida (LED incorporado)
led = Pin(2, Pin.OUT)

# Parpadeo con diferentes intervalos
intervalos = [0.1, 0.5, 1.0, 1.5]  # Intervalos en segundos

while True:
    for intervalo in intervalos:
        led.value(1)  # Encender el LED
        sleep(intervalo)
        led.value(0)  # Apagar el LED
        sleep(intervalo)