from machine import Pin,SoftI2C
from time import sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import dht

i2c=SoftI2C(scl=Pin(22), sda=Pin(21), freq=4000)
pantalla=I2cLcd(i2c, 0x27, 2, 16)
sensor=dht.DHT11(Pin(13))
led_verde=Pin(15,Pin.OUT)
led_amarillo=Pin(4,Pin.OUT)
led_rojo=Pin(5,Pin.OUT)
 
pantalla.move_to(2,0)
pantalla.putstr("San Miguel de")
pantalla.move_to(5,1)
pantalla.putstr("Tucuman")
sleep(2)
pantalla.clear()
gota = bytearray ([
  0B00000,
  0B00100,
  0B01010,
  0B10001,
  0B11111,
  0B11111,
  0B01110,
  0B00000	  					# ⬛⬜⬜⬜⬛ = 0x11
])
grados=bytearray([
     0B01111,
     0B01001,
     0B01001,
     0B01111,
     0B00000,
     0B00000,
     0B00000,
     0B00000
     ])
pantalla.custom_char(0, gota)
pantalla.custom_char(1,grados)
while True:
  
    sensor.measure()
    temperatura= sensor.temperature()
    humedad= sensor.humidity()
    pantalla.clear()
    pantalla.move_to(2,0)
    pantalla.putstr(f"Temp: {temperatura} {chr(1)}C")
    pantalla.move_to(0,1)
    pantalla.putstr(f"Humedad: {humedad} % {chr(0)}")
    if 0 < temperatura <= 25:
        led_verde.value(True)
        led_amarillo.value(False)
        led_rojo.value(False)
    if 25 <temperatura<= 38:
        led_verde.value(False)
        led_amarillo.value(True)
        led_rojo.value(False)
    if 38 <temperatura <50:
        led_verde.value(False)
        led_amarillo.value(False)
        led_rojo.value(True)
    sleep(1)
    