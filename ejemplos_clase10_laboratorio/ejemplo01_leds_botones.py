##########################################
#             Importaciones              #
##########################################

from machine import Pin, PWM
from time import sleep_ms

##########################################
#          Definicion de pines           #
##########################################

# Defino pines de los LEDs y botones
led_pins = [
    Pin(14, Pin.OUT),
    Pin(27, Pin.OUT),
    Pin(26, Pin.OUT),
    Pin(25, Pin.OUT)
    ]
boton_pins = [
    Pin(15, Pin.IN, Pin.PULL_UP),
    Pin(4, Pin.IN, Pin.PULL_UP),
    Pin(5, Pin.IN, Pin.PULL_UP),
    Pin(18, Pin.IN, Pin.PULL_UP)
    ]

# Pin del speaker (PWM)
speaker_pin = PWM(Pin(23))

# Silencio el speaker
speaker_pin.duty(0)

##########################################
#        Definicion de funciones         #
##########################################

# Función para reproducir un tono
def tono(frecuencia, duracion_ms):
  if frecuencia > 0:
      speaker_pin.freq(frecuencia)
      speaker_pin.duty(500)  # 50% de ciclo de trabajo
      sleep_ms(duracion_ms)
      speaker_pin.duty(0)  # Apagar sonido
  else:
      sleep_ms(duracion_ms)

##########################################
#    Comienzo del programa principal     #
##########################################

while True:
    # Comprobar si se ha presionado algún botón
    if not boton_pins[0].value():  # Si se presiona el botón rojo
        led_pins[0].on()
        tono(500,500)
        led_pins[0].off()
    if not boton_pins[1].value():  # Si se presiona el botón amarillo
        led_pins[1].on()
        tono(600,500)
        led_pins[1].off()
    if not boton_pins[2].value():  # Si se presiona el botón verde
        led_pins[2].on()
        tono(700,500)
        led_pins[2].off()
    if not boton_pins[3].value():  # Si se presiona el botón azul
        led_pins[3].on()
        tono(800,500)
        led_pins[3].off()
    sleep_ms(50)
