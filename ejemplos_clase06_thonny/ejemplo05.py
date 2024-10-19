# Este ejemplo utiliza PWM (modulación por ancho de pulso) para controlar el brillo del LED.

from machine import Pin, PWM
from time import sleep

# Configurar el pin GPIO 2 como salida PWM (LED incorporado)
led = PWM(Pin(2), freq=1000)

# Controlar el brillo del LED
while True:
    for duty in range(0, 1024, 10):  # Aumentar el brillo
        led.duty(duty)
        sleep(0.025)
    for duty in range(1023, -1, -10):  # Disminuir el brillo
        led.duty(duty)
        sleep(0.025)