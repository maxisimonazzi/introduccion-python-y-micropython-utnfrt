import time
from sensor_dht22 import medir_temperatura, medir_humedad
from oled_display import mostrar_datos

while True:
    temp = medir_temperatura()
    time.sleep(0.5) # Evita errores en la toma de mediciones
    hum = medir_humedad()
    
    if temp is not None:
        print('Temperatura: {}°C'.format(temp))
    if hum is not None:
        print('Humedad: {}%'.format(hum))
    mostrar_datos(temp, hum)
    
    # Esperar 2 segundos antes de la siguiente lectura
    time.sleep(2)