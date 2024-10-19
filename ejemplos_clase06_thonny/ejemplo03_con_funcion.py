# Encender y apagar el led incorporado

from machine import Pin
from time import sleep

# Configurar el pin GPIO 2 como salida (LED incorporado)
led = Pin(2, Pin.OUT)

# Funcion que invierte el valor del led
def toggle(p):
    p.value(not p.value())

# Bucle infinito para parpadear el LED
while True:
    toggle(led)
    sleep(1)