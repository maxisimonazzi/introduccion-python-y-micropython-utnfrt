import network
import time

ap = network.WLAN(network.AP_IF)
ap.active(True)

nombre = 'Mi_ESP32_AP'
contrasena = '1234567890'

ap.config(essid=nombre, password=contrasena, authmode=network.AUTH_WPA_WPA2_PSK)

# IP, máscara de red, puerta de enlace y DNS
ap.ifconfig(('192.168.56.1', '255.255.255.0', '192.168.56.1', '192.168.56.1'))

print('Punto de acceso configurado:')
print("-"*40)
print('SSID:', nombre)
print('IP:', ap.ifconfig()[0])
print('Máscara de red:', ap.ifconfig()[1])
print('Puerta de enlace:', ap.ifconfig()[2])
print('DNS:', ap.ifconfig()[3])
print("-"*40)

dispositivos_conectados = []

while True:
    dispositivo_nuevo = ap.status('stations')
    mac_nueva = []
    for dispositivos in dispositivo_nuevo:
        mac_address = ':'.join('%02x' % b for b in dispositivos[0])
        mac_nueva.append(mac_address)
    
    for mac in mac_nueva:
        if mac not in dispositivos_conectados:
            dispositivos_conectados.append(mac)
            print(f"Dispositivo conectado: {mac}")
    
    for mac in dispositivos_conectados[:]:
        if mac not in mac_nueva:
            dispositivos_conectados.remove(mac)
            print(f"Dispositivo desconectado: {mac}")
    time.sleep(5)
