from machine import Pin, PWM
from dcmotor import DCMotor
import time
import espnow
import network

# Inicializar red y ESPNOW
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

esp = espnow.ESPNow()
esp.active(True)

# Configuración del Motor A
in1A = Pin(5, Pin.OUT)  # Cambia por el pin que uses
in2A = Pin(18, Pin.OUT) # Cambia por el pin que uses
enaA = PWM(Pin(19))     # Cambia por el pin que uses
enaA.freq(15000)        # Frecuencia de 15 kHz para el motor
motorA = DCMotor(in1A, in2A, enaA)

# Configuración del Motor B
in1B = Pin(23, Pin.OUT) # Cambia por el pin que uses
in2B = Pin(22, Pin.OUT) # Cambia por el pin que uses
enaB = PWM(Pin(21))     # Cambia por el pin que uses
enaB.freq(15000)        # Frecuencia de 15 kHz para el motor
motorB = DCMotor(in1B, in2B, enaB)

try:
    while True:
        # Motor A hacia adelante, motor B detenido
        motorA.forward(50)  # Velocidad 50%
        motorB.stop()       # Detener motor B
        print("Motor A avanzando, Motor B detenido")
        time.sleep(2)

        # Motor B hacia adelante, motor A detenido
        motorA.stop()       # Detener motor A
        motorB.forward(50)  # Velocidad 50%
        print("Motor B avanzando, Motor A detenido")
        time.sleep(2)

        # Ambos motores hacia adelante
        motorA.forward(50)  # Velocidad 50%
        motorB.forward(50)  # Velocidad 50%
        print("Ambos motores avanzando")
        time.sleep(2)

except KeyboardInterrupt:
    # Detener ambos motores si se interrumpe el programa
    motorA.stop()
    motorB.stop()
    print("Programa detenido")