import network

estacion = network.WLAN(network.STA_IF)
estacion.active(True)

redes = estacion.scan()

print("Redes disponibles:")

for red in redes:
    ssid = red[0].decode('utf-8')
    bssid = ':'.join('%02x' % b for b in red[1])
    channel = red[2]
    rssi = red[3]
    authmode = red[4]
    authmodes = ['OPEN', 'WEP', 'WPA-PSK', 'WPA2-PSK', 'WPA/WPA2-PSK']
        
    print("-"*40)
    print(f"SSID: {ssid}")
    print(f"BSSID: {bssid}")
    print(f"Channel: {channel}")
    print(f"RSSI: {rssi}")
    print(f"Authentication: {authmodes[authmode]}")

estacion.active(False)