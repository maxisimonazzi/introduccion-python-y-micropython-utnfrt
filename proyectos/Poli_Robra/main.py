import network
import socket
import time
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20

# Configuración de los pines y sensores
ONE_WIRE_BUS = 4
ow = OneWire(Pin(ONE_WIRE_BUS))
ds = DS18X20(ow)

# Configuración de la red WiFi
ssid = '15888-PROVIDERS'
password = 'prov15888'

# Conexión a la red WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Conectando a WiFi...')
        time.sleep(1)
    print('Conectado a WiFi')
    print('Dirección IP:', wlan.ifconfig()[0])

# Configuración del servidor
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Servidor iniciado en', addr)
    return s

# Función principal
def main():
    connect_wifi()
    server = start_server()
    
    while True:
        cl, addr = server.accept()
        print('Cliente conectado desde', addr)
        request = cl.recv(1024)
        request = str(request)
        
        if 'GET' in request:
            ds.convert_temp()
            time.sleep(1)
            temp1 = ds.read_temp(ds.scan()[0])
            temp2 = ds.read_temp(ds.scan()[1])
            
            response = f"""HTTP/1.1 200 OK
Content-Type: text/plain
Connection: close

Temp1: {temp1} C
Temp2: {temp2} C
"""
            cl.send(response)
            cl.close()

if __name__ == '__main__':
    main()