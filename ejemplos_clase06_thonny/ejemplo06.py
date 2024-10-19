# Este ejemplo hace que el LED parpadee con una frecuencia que varía con el tiempo.

from machine import Pin
from time import sleep

# Configurar el pin GPIO 2 como salida (LED incorporado)
led = Pin(2, Pin.OUT)

# Frecuencia inicial y paso de incremento
frecuencia = 0.1
paso = 0.05

while True:
    led.value(1)  # Encender el LED
    sleep(frecuencia)
    led.value(0)  # Apagar el LED
    sleep(frecuencia)
    
    # Incrementar la frecuencia
    frecuencia += paso
    if frecuencia > 1.0 or frecuencia < 0.1:
        paso = -paso  # Invertir la dirección del cambio de frecuencia