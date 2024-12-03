import machine
import time
import dht

# Configurar pin de conexion DHT22
dht_pin = machine.Pin(14)

# Crear un objeto DHT22
sensor = dht.DHT22(dht_pin)

while True:
    try:
        # Leer los datos del sensor
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Imprimir los valores
        print('Temperatura: {}°C'.format(temp))
        print('Humedad: {}%'.format(hum))
        
    except OSError as e:
        print('Error al leer el sensor:', e)
    
    # Esperar 2 segundos antes de la siguiente lectura
    time.sleep(2)