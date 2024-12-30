import network
from machine import Pin
import espnow
import utime


# Activar la interfaz de red para ESPNOW
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# Inicializar ESPNOW
esp = espnow.ESPNow()
esp.active(True)

# Dirección MAC del ESP32 receptor
peer = b'\xb8\xd6\x1aBU\x00'  # Asegúrate de cambiar esto por la MAC de tu receptor
esp.add_peer(peer)

# Configurar los botones
button_UP = Pin(16, Pin.IN, Pin.PULL_UP)
button_LEFT = Pin(17, Pin.IN, Pin.PULL_UP)
button_RIGHT = Pin(18, Pin.IN, Pin.PULL_UP)

# Variables para debounce
last_button_UP_state = 1  # Estado inicial del botón (no presionado)
last_button_LEFT_state = 1  # Estado inicial del botón
last_button_RIGHT_state = 1  # Estado inicial del botón
debounce_delay = 50  # Retardo para debounce en milisegundos

while True:
    # Leer el estado de cada botón
    button_UP_state = button_UP.value()
    button_LEFT_state = button_LEFT.value()
    button_RIGHT_state = button_RIGHT.value()

    # Verificar si el estado del botón UP ha cambiado
    if button_UP_state != last_button_UP_state:
        utime.sleep_ms(debounce_delay)  # Esperar para debounce
        if button_UP.value() == 0:  # Verificar si sigue presionado
            esp.send(peer, b'UP')  # Enviar comando UP
            print("Enviando comando: UP")
        last_button_UP_state = button_UP_state  # Actualizar el último estado

    # Verificar si el estado del botón LEFT ha cambiado
    if button_LEFT_state != last_button_LEFT_state:
        utime.sleep_ms(debounce_delay)
        if button_LEFT.value() == 0:
            esp.send(peer, b'LEFT')  # Enviar comando LEFT
            print("Enviando comando: LEFT")
        last_button_LEFT_state = button_LEFT_state

    # Verificar si el estado del botón RIGHT ha cambiado
    if button_RIGHT_state != last_button_RIGHT_state:
        utime.sleep_ms(debounce_delay)
        if button_RIGHT.value() == 0:
            esp.send(peer, b'RIGHT')  # Enviar comando RIGHT
            print("Enviando comando: RIGHT")
        last_button_RIGHT_state = button_RIGHT_state

    utime.sleep_ms(10)  # Pausa breve para reducir la carga del CPU