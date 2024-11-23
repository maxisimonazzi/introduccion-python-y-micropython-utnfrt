##########################################
#             Importaciones              #
##########################################

from machine import Pin, PWM
from utime import sleep
import urequests
import network

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

# Defino pin del speaker (PWM)
speaker_pin = PWM(Pin(23))

# Silencio el speaker
speaker_pin.duty(0)

##########################################
#            Conexion Wi-Fi              #
##########################################

ssid = "xxx"
password = "yyy"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Conectando...")
    sleep(1)

print("Conectado a Wi-Fi:", wlan.ifconfig())

##########################################
#        Definicion de funciones         #
##########################################

def url_encode(data):
    encoded_data = []
    for key, value in data.items():
        encoded_key = key.replace(" ", "%20")
        encoded_value = value.replace(" ", "%20")
        encoded_data.append(f"{encoded_key}={encoded_value}")
    return "&".join(encoded_data)

def enviar_mensaje():
    url = "https://api.callmebot.com/whatsapp.php"
    # Colocar telefono y API key obtenida con el bot
    data = {
        "phone": "549xxxxx12",
        "text": "Boton activado.",
        "apikey": "xxxx"
    }
    data_encoded = url_encode(data)
    full_url = f"{url}?{data_encoded}"
    response = urequests.post(full_url)
    print("Respuesta del servidor:", response.text)
    response.close()

##########################################
#    Comienzo del programa principal     #
##########################################

while True:
    for i, boton in enumerate(boton_pins):
        if boton.value() == 0:  # Si el botón está presionado
            print(f"Mandando mensaje desde el botón {i}")
            enviar_mensaje()
            sleep(2)