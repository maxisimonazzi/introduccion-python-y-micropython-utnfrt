import network
import urequests
import time

def conectar_wifi():
    
    ssid = 'CEO_WiFi'
    password = 'abc12345'

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

def obtener_hora_actual():
    try:
        respuesta = urequests.get('http://worldtimeapi.org/api/timezone/America/Argentina/Tucuman')
        if respuesta.status_code == 200:
            data = respuesta.json()
            respuesta.close()
            return data['datetime']
        else:
            print('Error al obtener la hora:', respuesta.status_code)
            return None
    except Exception as e:
        print('Error al conectar con la API:', e)
        return None
