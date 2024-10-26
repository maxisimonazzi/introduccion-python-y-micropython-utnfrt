from machine import Pin
from time import sleep
from dht import DHT22 

sensor = DHT22(Pin(13))

while True:
    sensor.measure() # Leemos los valores del sensor
    temperatura = sensor.temperature() # Obtenemos la temperatura
    humedad = sensor.humidity() # Obtenemos la humedad
    print('\033[2J\033[H') # Limpiamos la pantalla
    print(f'Temperatura: {temperatura} ºC')
    print(f'Humedad: {humedad} %')
    sleep(1)