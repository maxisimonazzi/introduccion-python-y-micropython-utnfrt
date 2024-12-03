import network
import urequests as requests
import time
from machine import Pin
from dht import DHT11
import gc

# Configuración Wi-Fi
ssid = "Familia_SF"
password = "xxxxxx"

# Configuración del Bot de Telegram
bot_token = "xxxxx:xxxxxx"
chat_id = "xxxxxx"

# Pines del ESP32
dht_sensor = DHT11(Pin(23))  # DHT11 conectado al GPIO23
rele = Pin(22, Pin.OUT)  # Relé o actuador conectado al GPIO22

# Estado inicial del relé o actuador (apagado)
rele.value(0)

# Conexión a Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print("WiFi conectado:", wlan.ifconfig())

# Verificar conexión Wi-Fi
def check_wifi():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Wi-Fi desconectado. Reconectando...")
        connect_wifi()

# Función para enviar mensajes a Telegram
def send_telegram_message(message, reply_markup=None):
    gc.collect()  # Liberar memoria antes de la operación
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    if reply_markup:
        payload["reply_markup"] = reply_markup
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        if response.status_code == 200:
            print("Mensaje enviado con éxito")
        else:
            print("Error al enviar mensaje:", response.text)
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")

# Función para mostrar el menú interactivo
def send_telegram_menu():
    reply_markup = {
        "keyboard": [
            ["Saber temperatura", "Saber humedad"],
            ["Encender equipo", "Apagar equipo"]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True
    }
    send_telegram_message("Selecciona una opción:", reply_markup)

# Función para medir la temperatura y la humedad
def medir_dht():
    gc.collect()  # Liberar memoria antes de la lectura
    for intento in range(3):  # Hasta 3 intentos
        try:
            dht_sensor.measure()
            return dht_sensor.temperature(), dht_sensor.humidity()
        except OSError:
            time.sleep(1)  # Esperar antes de reintentar
    return None, None

# Función para obtener actualizaciones de Telegram
def get_telegram_updates(last_update_id):
    gc.collect()  # Liberar memoria antes de la consulta
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates?offset={last_update_id + 1}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()["result"]
        else:
            print("Error al obtener actualizaciones:", response.text)
            return []
    except Exception as e:
        print(f"Error en la petición de actualizaciones: {e}")
        return []

# Procesar mensajes de Telegram
def process_message(message):
    text = message.get("text", "").strip().lower()
    if text == "saber temperatura":
        temp, _ = medir_dht()
        send_telegram_message(f"La temperatura es {temp}°C" if temp is not None else "Error al leer el sensor.")
    elif text == "saber humedad":
        _, hum = medir_dht()
        send_telegram_message(f"La humedad es {hum}%" if hum is not None else "Error al leer el sensor.")
    elif text == "encender equipo":
        rele.value(1)  
        send_telegram_message("El equipo ha sido encendido.")
    elif text == "apagar equipo":
        rele.value(0)  
        send_telegram_message("El equipo ha sido apagado.")
    else:
        send_telegram_message("Comando no reconocido. Usa las opciones del menú.")
    send_telegram_menu()  

# Conectar al Wi-Fi
connect_wifi()


last_update_id = 0


send_telegram_menu()

# Bucle principal
while True:
    check_wifi()  
    updates = get_telegram_updates(last_update_id)
    for update in updates:
        message = update.get("message")
        if message:
            print(f"Nuevo mensaje: {message['text']}")
            process_message(message)  
            last_update_id = update["update_id"]  
    time.sleep(2)  
