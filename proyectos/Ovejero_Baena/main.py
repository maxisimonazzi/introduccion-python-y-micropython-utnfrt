import time
from lib.net import conectar_wifi  
from lib.net import obtener_hora_actual  
from lib.sensor_dht22 import medir_temperatura, medir_humedad
from lib.oled_display import mostrar_datos


conectar_wifi


while True:
    temp = medir_temperatura()
    time.sleep(0.5) # Evita errores en la toma de mediciones
    hum = medir_humedad()
    
    time.sleep(1)
    datos_hora = obtener_hora_actual()

    if datos_hora is not None:
        print('Hora: {}'.format(datos_hora))
    if temp is not None:
        print('Temperatura: {}°C'.format(temp))
    if hum is not None:
        print('Humedad: {}%'.format(hum))
    mostrar_datos(temp, hum)

# Esperar 2 segundos antes de la siguiente lectura
    time.sleep(2)        