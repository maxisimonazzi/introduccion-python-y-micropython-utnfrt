from machine import Pin
from time import sleep

import dht 

# Configuración de pines
sensor = dht.DHT11(Pin(32))
boton = Pin(25, Pin.IN, Pin.PULL_UP)
led_rojo = Pin(5, Pin.OUT)
led_amarillo = Pin(4, Pin.OUT)
led_verde = Pin(15, Pin.OUT)
bomba_pin = Pin(33, Pin.OUT)  # Pin para la bomba de agua

# Inicialización de variables
bandera = 0
humedad = 0
bomba_agua = 0

while True:
    sleep(2)
    # Detecta si el botón está presionado
    if boton.value() == 0:
        print("boton")
        # Cambia el estado de bandera en ciclo
        if bandera == 0:
            bandera = 1
        elif bandera == 1:
            bandera = 2
        elif bandera == 2:
            bandera = 0

    try:
        # Medir humedad y temperatura
        sensor.measure()
        humedad = sensor.humidity()
        print(f'Humedad: {humedad}%')

        # Control de LEDs y bomba según el estado de la bandera
        if bandera == 0:  # Sistema en flora
            led_rojo.on()
            led_amarillo.off()
            led_verde.off()
            print("Estado: Flora (LED rojo)")
            if  humedad < 35:
                bomba_pin.on()
                print("bomba")
            else:
                bomba_pin.off()
                print("no bomba")

            

        elif bandera == 1:  # Sistema en vegetación
            led_rojo.off()
            led_amarillo.on()
            led_verde.off()
            print("Estado: Vegetación (LED amarillo)")
            if humedad < 40:
                print("bomba")
            else:
                bomba_pin.off()
                print("no bomba")
       

        elif bandera == 2:  # Sistema en plántula
            led_rojo.off()
            led_amarillo.off()
            led_verde.on()
            print("Estado: Plántula (LED verde)")
            if humedad < 90:
                bomba_pin.on()
                print("bomba")
            else:
                bomba_pin.off()
                print("no bomba")

    except OSError as e:
        print(f"Error al leer el sensor: {e}")


        
        
        
     