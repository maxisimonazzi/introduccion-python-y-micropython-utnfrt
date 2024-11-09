from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(scl=Pin(21), sda=Pin(22), freq=1000000)

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hola curso!', 10, 5)
oled.text('Micropython', 20, 25)
oled.text('UTN - FRT', 30, 45)
oled.show()