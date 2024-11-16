import network
import urequests
import time

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
print('Conectado')
print("-"*40)
print('Configuración de red:')
print(f"IP: {config[0]}")
print(f"Mascara de red: {config[1]}")
print(f"Gateway: {config[2]}")
print(f"DNS: {config[3]}")
print("-"*40)

respuesta = urequests.get('http://www.google.com')

if respuesta.status_code == 200:
    print('El sitio www.google.com respondio correctamente, por lo que estas conectado a internet.')
    respuesta.close()
else:
    print('El sitio www.google.com no respondio, por lo que no estas conectado a internet.')
    respuesta.close()
