import network
import socket
from machine import ADC, Pin
import math
import random
import time

# Configuración de los sensores MQ135
mq135_input = ADC(Pin(32))  # Sensor entrada (GPIO32)
mq135_output = ADC(Pin(33))  # Sensor salida (GPIO33)
mq135_input.atten(ADC.ATTN_11DB)  # Rango de 0-3.6V
mq135_output.atten(ADC.ATTN_11DB)

# Variables dinámicas para temperatura y humedad
temperature = 24  # Temperatura inicial
humidity = 93     # Humedad inicial
time_counter = 0  # Contador de minutos simulados

# Resistencia de carga (en ohmios) y calibración
RL = 10000  # 10kΩ
RO = 10000  # Calibración en aire limpio

# Configuración del Access Point
SSID = "PURIFICADOR"
PASSWORD = "12345678"

# Función para convertir ADC a voltaje
def adc_to_voltage(adc_value):
    return adc_value * 3.3 / 4095

# Función para calcular Rs
def calculate_rs(adc_value, rl=RL):
    voltage = adc_to_voltage(adc_value)
    if voltage == 0:
        return float('inf')  # Para evitar división por 0
    return rl * ((3.3 - voltage) / voltage)

# Función para calcular Rs/Ro
def calculate_ratio(rs, ro=RO):
    return rs / ro

# Función para calcular PPM
def calculate_ppm(rs_ro_ratio, a=-0.32, b=1.0):
    return math.pow(10, (a * math.log10(rs_ro_ratio) + b))

# Leer y calcular valores de los sensores MQ135
def read_mq135_sensors():
    adc_in = mq135_input.read()
    adc_out = mq135_output.read()
    
    rs_in = calculate_rs(adc_in)
    rs_out = calculate_rs(adc_out)
    
    ratio_in = calculate_ratio(rs_in)
    ratio_out = calculate_ratio(rs_out)
    
    ppm_in = calculate_ppm(ratio_in)
    ppm_out = calculate_ppm(ratio_out)
    
    return ppm_in, ppm_out

# Función para simular temperatura
def simulate_temperature(counter):
    global temperature
    # Cambia la temperatura cada 15 minutos en el ciclo 24 -> 23 -> 22 -> 21
    steps = [24, 23, 22, 21]
    index = (counter // 15) % len(steps)
    temperature = steps[index]
    return temperature

# Función para simular humedad
def simulate_humidity(counter):
    global humidity
    # Cambia humedad de forma aleatoria cada 15 minutos
    if counter % 15 == 0:
        humidity = random.randint(89, 97)
    return humidity

# Configuración del Access Point
def configurar_ap(ssid, password):
    ap = network.WLAN(network.AP_IF)  # Modo Access Point
    ap.active(True)
    ap.config(essid=ssid, password=password)  # Configura la red Wi-Fi del AP
    print(f"Red Wi-Fi '{ssid}' creada.")
    print(f"Dirección IP: {ap.ifconfig()[0]}")
    return ap.ifconfig()[0]

# Servidor Web
def start_server(ip_address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_address, 80))  # Escucha en el puerto 80
    s.listen(5)
    print(f"Servidor web iniciado en: http://{ip_address}")

    global time_counter

    while True:
        conn, addr = s.accept()
        print(f"Conexión desde: {addr}")
        request = conn.recv(1024).decode()
        print(f"Solicitud recibida: {request}")

        # Simular valores dinámicos
        temperature_now = simulate_temperature(time_counter)
        humidity_now = simulate_humidity(time_counter)

        # Leer valores de los sensores MQ135
        ppm_in, ppm_out = read_mq135_sensors()

        # Incrementar contador cada minuto simulado
        time_counter += 1

        # Respuesta HTML
        html_response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html>
    <head>
        <title>PURIFICADOR DE AIRE</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; }}
            header {{ background-color: #ffffff; color: orange; padding: 1rem; text-align: center; border-bottom: 3px solid orange; }}
            main {{ padding: 1rem; text-align: center; }}
            .sensor {{ margin: 2rem 0; }}
            .value {{ font-size: 2rem; font-weight: bold; }}
            footer {{ background-color: #222; color: white; padding: 1rem; text-align: center; }}
        </style>
    </head>
    <body>
        <header><h1>PURIFICADOR DE AIRE</h1></header>
        <main>
            <div class="sensor"><div>🌬 Entrada: {ppm_in:.2f} PPM</div></div>
            <div class="sensor"><div>🌬 Salida: {ppm_out:.2f} PPM</div></div>
            <div class="sensor"><div>🌡 Temperatura: {temperature_now:.2f} °C</div></div>
            <div class="sensor"><div>💧 Humedad: {humidity_now:.2f} %</div></div>
        </main>
        <footer><p>Diseñado por Equipo Mecatrónica &copy; 2024</p></footer>
    </body>
</html>
"""
        conn.send(html_response.encode())
        conn.close()
        time.sleep(1)  # Simula 1 minuto por iteración

# Configurar Access Point y ejecutar servidor
ip_address = configurar_ap(SSID, PASSWORD)
start_server(ip_address)