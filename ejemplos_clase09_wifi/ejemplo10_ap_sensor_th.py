from machine import Pin
import network
import socket
from dht import DHT11

sensor = DHT11(Pin(13))

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
    response = f"""\
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
    <h2>IP: {ip}</h1>
    <h2>Máscara de red: {mascara_subred}</h1>
    <h2>Puerta de enlace: {puerta_enlace}</h1>
    <h2>DNS: {dns}</h1>
    <p></p>
    <hr>
    <h1>Cliente conectado desde</h1>
    <p></p>
    <h2>IP: {ip_cliente[0]}</h1>
    <h2>Puerto socket en cliente: {ip_cliente[1]}</h1>
    <p></p>
    <hr>
    <h1>Valores del sensor DHT11</h1>
    <p></p>
    <h2>Temperatura: {temperatura}</h1>
    <h2>Humedad: {humedad}</h1>
    <p></p>
    <hr>
    <h1>Fin de la página</h1>
</body>
</html>
"""
    cliente.send(response)
    cliente.close()