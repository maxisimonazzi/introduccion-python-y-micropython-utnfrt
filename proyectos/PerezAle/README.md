# Proyecto Invernadero Simulado con ESP32 y MicroPython

## Descripción

Este proyecto simula el funcionamiento de un sistema de invernadero controlado por un microcontrolador ESP32 utilizando el lenguaje de programación MicroPython. El sistema simula el ciclo de crecimiento de plantas, cada una con diferentes necesidades de humedad en cada etapa de su desarrollo. 

A través de un sensor DHT11, se mide la humedad ambiente del invernadero y, en función del estado de crecimiento de la planta, se activa o desactiva una bomba de agua (representada por un LED azul) para mantener la humedad dentro de los rangos necesarios.

## Funcionalidad

El sistema cuenta con tres etapas de crecimiento para las plantas, que corresponden a los siguientes estados:

1. **Flora** (Estado inicial de la planta): 
   - LED Rojo encendido.
   - La bomba se activa si la humedad es menor al 35%.

2. **Vegetación**: 
   - LED Amarillo encendido.
   - La bomba se activa si la humedad es menor al 40%.

3. **Plántula**: 
   - LED Verde encendido.
   - La bomba se activa si la humedad es menor al 90%.

A través de un botón, se puede cambiar entre los diferentes estados de crecimiento de las plantas, lo que permite simular el control del sistema en función de las necesidades de humedad en cada etapa.

## Componentes

- **ESP32**: Microcontrolador que ejecuta el código en MicroPython.
- **DHT11**: Sensor de temperatura y humedad para medir las condiciones del ambiente.
- **LEDs**: Indicadores visuales para mostrar el estado de la planta (rojo, amarillo, verde).
- **Bomba de agua**: Representada por un LED azul, activa cuando la humedad está por debajo del umbral necesario para la etapa de crecimiento correspondiente.
- **Botón**: Permite cambiar el estado de crecimiento de la planta.

## Diagrama de conexiones

- DHT11 conectado al pin GPIO32 del ESP32.
- LEDs conectados a los pines GPIO5, GPIO4 y GPIO15 del ESP32.
- Bomba de agua (LED azul) conectada al pin GPIO33.
- Botón conectado al pin GPIO25 del ESP32.

## Instalación
Para ejecutar este proyecto, necesitas tener configurado el entorno de MicroPython en tu ESP32. Sigue estos pasos:

Instala MicroPython en tu ESP32 siguiendo esta guía oficial.
Conecta los componentes electrónicos según el diagrama de conexiones mencionado.
Carga el código a tu ESP32 usando un editor como Thonny o uPyCraft.

## Autor
Este proyecto fue realizado por Joaquín Tomás Pérez Ale como parte del curso Introducción a Python y MicroPython de la Universidad Tecnológica Nacional, Facultad Regional Tucumán.

Puedes contactarme en joaquinperezale@gmail.com.

## Link video 
https://youtu.be/Jxyz2f6-LTg

## Código

```python
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


