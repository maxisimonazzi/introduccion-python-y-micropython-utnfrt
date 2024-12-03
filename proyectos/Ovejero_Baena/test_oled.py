from machine import Pin, SoftI2C
import ssd1306
import time

# Configurar I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# Inicializar la pantalla OLED
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Función para mostrar texto y números en la pantalla
def mostrar_texto():
    oled.fill(0)  # Limpiar la pantalla
    oled.text('Hola, Mundo!', 0, 0)
    oled.text('MicroPython', 0, 10)
    oled.text('SSD1306 OLED', 0, 20)
    oled.text('1234567890', 0, 30)
    oled.show()

# Llamar a la función para mostrar el texto
mostrar_texto()

# Mantener el texto en pantalla por 10 segundos
time.sleep(10)

# Limpiar la pantalla después de la prueba
oled.fill(0)
oled.show()