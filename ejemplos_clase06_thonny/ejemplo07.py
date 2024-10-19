from machine import Pin
from time import sleep

# Configurar el pin GPIO 2 como salida (LED incorporado)
led = Pin(2, Pin.OUT)

# Configurar el pin GPIO 0 como entrada (Botón BOOT)
boton = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    if boton.value() == 0:  # Si el botón está presionado
        led.value(1)  # Encender el LED
    else:
        led.value(0)  # Apagar el LED
        
    sleep(0.1)  # Esperar un poco antes de verificar nuevamente