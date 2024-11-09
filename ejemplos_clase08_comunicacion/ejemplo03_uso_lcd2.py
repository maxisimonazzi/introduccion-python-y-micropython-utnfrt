import machine
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

i2c = machine.SoftI2C(sda=machine.Pin(19), scl=machine.Pin(18), freq=1000000)

lcd = I2cLcd(i2c, 0x27, 2, 16)

nene = bytearray ([
  0b01110,							# ⬜⬛⬛⬛⬜ = 0x0E
  0b01010,							# ⬜⬛⬜⬛⬜ = 0x0A
  0b01110,							# ⬜⬛⬛⬛⬜ = 0x0E
  0b11111,							# ⬛⬛⬛⬛⬛ = 0x1F
  0b00100,							# ⬜⬜⬛⬜⬜ = 0x04
  0b00100,							# ⬜⬜⬛⬜⬜ = 0x04
  0b01010,							# ⬜⬛⬛⬛⬜ = 0x0E
  0b10001					   		# ⬛⬜⬜⬜⬛ = 0x11
])

smile = bytearray([0x00, 0x00, 0x0A, 0x00, 0x11, 0x0E, 0x00, 0x00])

lcd.custom_char(0, nene)
lcd.custom_char(1, smile)

lcd.move_to(0,0)
lcd.putstr(f"Micropython ! {chr(0)}{chr(0)}")

lcd.move_to(2,1)
lcd.putstr(f"{chr(1)} UTN-FRT {chr(1)}")