from machine import Pin, PWM
import time

# Configurar el pin GPIO15 como salida PWM
led = PWM(Pin(15))

# Configurar la frecuencia del PWM a 1 kHz (1000 Hz)
led.freq(1000)

# Bucle infinito para cambiar el brillo del LED
while True:
    # Aumentar el brillo de 0 a 1023
    for ciclo in range(0, 1024, 10):
        led.duty(ciclo)  # Configurar el ciclo de trabajo (duty cycle)
        print(led.duty()) # Mostrar el ciclo de trabajo seteado en ese momento
        time.sleep(0.01)  # Esperar 10 ms

    # Disminuir el brillo de 1023 a 0
    for ciclo in range(1023, 0, -10):
        led.duty(ciclo)  # Configurar el ciclo de trabajo (duty cycle)
        print(led.duty()) # Mostrar el ciclo de trabajo seteado en ese momento
        time.sleep(0.01)  # Esperar 10 ms