import network
import espnow
import utime
from machine import Pin, PWM
from dcmotor import DCMotor

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

def handle_command(command):
    """Procesa el comando recibido para controlar los motores."""
    if command == b'UP':
        print("Adelante: Ambos motores avanzan")
        motorA.forward(50)  # Motor A avanza al 50%
        motorB.forward(50)  # Motor B avanza al 50%
    elif command == b'RIGHT':
        print("Giro a la derecha: Motor A avanza, Motor B detenido")
        motorA.forward(50)  # Motor A avanza
        motorB.stop()       # Motor B detenido
    elif command == b'LEFT':
        print("Giro a la izquierda: Motor B avanza, Motor A detenido")
        motorA.stop()       # Motor A detenido
        motorB.forward(50)  # Motor B avanza
    else:
        print(f"Mensaje desconocido: {command}")
        motorA.stop()
        motorB.stop()

# Bucle principal
while True:
    # Recepción de mensajes
    _, msg = esp.recv()
    if msg:  # Si hay mensaje recibido
        handle_command(msg)  # Procesar el comando

    # Pequeña pausa para evitar saturación
    utime.sleep_ms(100)