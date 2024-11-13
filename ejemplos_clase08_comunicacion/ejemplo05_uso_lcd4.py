from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from dht import DHT22 

i2c = SoftI2C(sda=Pin(19), scl=Pin(18), freq=500000)

lcd1 = I2cLcd(i2c, 0x11, 2, 16)
lcd2 = I2cLcd(i2c, 0x27, 2, 16)


sensor = DHT22(Pin(13))

nene = bytearray ([0x0E, 0x0A, 0x0E, 0x1F, 0x04, 0x04, 0x0E, 0x11])
smile = bytearray([0x00, 0x00, 0x0A, 0x00, 0x11, 0x0E, 0x00, 0x00])
grados = bytearray([ 0x07, 0x05, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00])

lcd1.custom_char(0, nene)
lcd2.custom_char(1, smile)
lcd1.custom_char(2, grados)

lcd1.move_to(0,0)
lcd1.putstr(f"! Micropython !")
lcd1.move_to(2,1)
lcd1.putstr(f"{chr(0)} {chr(0)} {chr(0)} {chr(0)} {chr(0)} {chr(0)}")

lcd2.move_to(0,0)
lcd2.putstr(f"!!  UTN-FRT  !!")
lcd2.move_to(6,1)
lcd2.putstr(f"{chr(1)} {chr(1)}")

sleep(2)

lcd1.clear()
lcd2.clear()

while True:
    sensor.measure() # Leemos los valores del sensor
    temperatura = sensor.temperature() # Obtenemos la temperatura
    humedad = sensor.humidity() # Obtenemos la humedad

    lcd1.move_to(0,0)
    lcd1.putstr(f'Temperatura')
    lcd1.move_to(9,1)
    lcd1.putstr(f'{temperatura} {chr(2)}C')

    lcd2.move_to(0,0)
    lcd2.putstr(f'Humedad')
    lcd2.move_to(10,1)
    lcd2.putstr(f'{humedad} %')

    sleep(1)
