from machine import Pin
import network
import socket
from dht import DHT11
import time
import urequests

sensor = DHT11(Pin(13))

# Configuración de la estación
ssid = 'nombre-red'
password = 'xxxx'
estacion = network.WLAN(network.STA_IF)
estacion.active(True)
estacion.connect(ssid, password)
print('Conectando ...', end="")
while not estacion.isconnected():
    print('.', end="")
    time.sleep(0.1)
config = estacion.ifconfig()

print()
print()
print('Conectado a la red:')
print("-"*40)
print(f"SSID: {ssid}")
print(f"IP: {config[0]}")
print(f"Mascara de red: {config[1]}")
print(f"Gateway: {config[2]}")
print(f"DNS: {config[3]}")

# Configuración del Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)
nombre = 'Mi_ESP32_AP'
contrasena = '1234567890'
ap.config(essid=nombre, password=contrasena, authmode=network.AUTH_WPA_WPA2_PSK)
ip = '10.0.0.15'
mascara_subred = '255.255.255.0'
puerta_enlace = '10.0.0.15'
dns = '10.0.0.15'
ap.ifconfig((ip, mascara_subred, puerta_enlace, dns))

print()
print('Punto de acceso configurado:')
print("-"*40)
print('SSID:', nombre)
print('IP:', ap.ifconfig()[0])
print('Máscara de red:', ap.ifconfig()[1])
print('Puerta de enlace:', ap.ifconfig()[2])
print('DNS:', ap.ifconfig()[3])
print("-"*40)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)

print()
print('Servidor web en ejecución...')
print("-"*40)

while True:
    cliente, ip_cliente = s.accept()
    print('Cliente conectado desde', ip_cliente)
    sensor.measure()
    temperatura = sensor.temperature()
    humedad = sensor.humidity()
    
    google = urequests.get('http://www.google.com')
    if google.status_code == 200:
        print('El sitio www.google.com respondio correctamente, por lo que estas conectado a internet.')
        google.close()
    else:
        print('El sitio www.google.com no respondio, por lo que no estas conectado a internet.')
        google.close()

    respuesta = f"""\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ESP32 AP</title>
</head>
<body>
    <h1>Hola mundo</h1>
    <p></p>
    <hr>
    <h1>Valores del Access Point</h1>
    <p></p>
    <h3>IP: {ip}</h3>
    <h3>Máscara de red: {mascara_subred}</h3>
    <h3>Puerta de enlace: {puerta_enlace}</h3>
    <h3>DNS: {dns}</h3>
    <p></p>
    <hr>
    <h1>Cliente conectado desde</h1>
    <p></p>
    <h3>IP: {ip_cliente[0]}</h3>
    <h3>Puerto socket en cliente: {ip_cliente[1]}</h3>
    <p></p>
    <hr>
    <h1>Valores del sensor DHT11</h1>
    <p></p>
    <h3>Temperatura: {temperatura}</h3>
    <h3>Humedad: {humedad}</h3>
    <p></p>
    <hr>
    <h1>Estado de conexión a internet</h1>
    <p></p>
    <h3>Estado de peticion: {google.status_code}</h3>
    <h3>El sitio www.google.com respondio, por lo que estas conectado a internet.</h3>
    <p></p>
</body>
</html>
"""
    cliente.send(respuesta)
    cliente.close()