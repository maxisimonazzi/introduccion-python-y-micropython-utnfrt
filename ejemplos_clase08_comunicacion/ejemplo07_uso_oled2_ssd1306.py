from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from dht import DHT22 
from time import sleep

i2c = SoftI2C(scl=Pin(21), sda=Pin(22), freq=1000000)
sensor = DHT22(Pin(13))

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.text('Hola curso!', 10, 5)
oled.text('Micropython', 20, 25)
oled.text('UTN - FRT', 30, 45)
oled.show()

sleep(2)

while True:
    sensor.measure() # Leemos los valores del sensor
    temperatura = sensor.temperature() # Obtenemos la temperatura
    humedad = sensor.humidity() # Obtenemos la humedad

    oled.fill(1)
    oled.text('Temperatura', 10,5,0)
    oled.text(f'{temperatura} C', 75,20,0)
    oled.text('Humedad', 10,35,0)
    oled.text(f'{humedad}%', 80,50,0)
    oled.show()
    sleep(0.5)
