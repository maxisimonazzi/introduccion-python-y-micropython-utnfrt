import machine
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

i2c = machine.SoftI2C(sda=machine.Pin(19), scl=machine.Pin(18), freq=1000000)

lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.move_to(2,0)
lcd.putstr("Micropython!")

lcd.move_to(4,1)
lcd.putstr("UTN-FRT!")