from machine import Pin
from utime import sleep

# Configurar los pines de los leds como salidas
led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(4, Pin.OUT)
led_rojo = Pin(5, Pin.OUT)

# Configurar los pines de los leds como entradas con resistencias de pull-up
boton = Pin(25, Pin.IN, Pin.PULL_UP)

cuenta = 0
advertencia = 0

while True:
    if boton.value() == 0:  # Si el botón está presionado
        cuenta += 1
        print(f"Apretaste el boton verde {cuenta} veces")
        sleep(0.5)
    if cuenta == 5 and advertencia == 0:
        print("No presiones el boton 10 veces")
        advertencia = 1
    if cuenta == 8 and advertencia == 1:
        print("En serio, no presiones 10 veces sino me voy a reiniciar.")
        advertencia = 2
    if cuenta == 9 and advertencia == 2:
        print("Una mas y me reinicio")
        advertencia = 3
    if cuenta == 10 and advertencia == 3:
        print("Listo, te lo ganaste.")
        print("Cuenta regresiva.")
        sleep(1)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        print("Iniciando reseteo")
        sleep(1)
        machine.reset()