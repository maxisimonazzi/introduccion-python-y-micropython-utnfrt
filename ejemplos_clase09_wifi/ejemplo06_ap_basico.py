import network
import time

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