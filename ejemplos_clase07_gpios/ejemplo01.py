from machine import Pin
from utime import sleep

verde = Pin(15, Pin.OUT)
amarillo = Pin(4, Pin.OUT)
rojo = Pin(5, Pin.OUT)

while True:
    # -- Led Verde -- #
    verde.on()
    sleep(0.5)
    verde.off()
    sleep(0.5)

    # -- Led Amarillo -- #
    amarillo.value(1)
    sleep(0.5)
    amarillo.value(0)
    sleep(0.5)

    # -- Led Rojo -- #
    rojo.value(True)
    sleep(0.5)
    rojo.value(False)
    sleep(0.5)