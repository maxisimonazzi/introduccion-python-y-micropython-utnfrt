from machine import Pin, ADC, PWM
import time

# Configuración de pines
sensor_humedad = ADC(Pin(34))  # Potenciómetro simula el sensor de humedad
sensor_humedad.atten(ADC.ATTN_11DB)  # Rango completo 0-3.3V
bomba = Pin(27, Pin.OUT)  # LED simula la bomba
buzzer = PWM(Pin(26))  # Buzzer para emitir sonidos

# Umbral de humedad para activar la bomba
UMBRAL_HUMEDAD = 70  # 70% de humedad

# Función para leer el sensor de humedad del suelo
def leer_humedad_suelo():
    valor_adc = sensor_humedad.read()  # Leer valor del potenciómetro (0-4095)
    humedad = (valor_adc / 4095) * 100  # Convertir a porcentaje (0-100)
    return round(humedad, 2)

# Función para generar pitidos con el buzzer
def beep(n):
    for _ in range(n):
        buzzer.freq(1000)  # Frecuencia del sonido en Hz
        buzzer.duty(512)  # Intensidad del sonido (50% del ciclo)
        time.sleep(0.2)
        buzzer.duty(0)  # Apagar buzzer
        time.sleep(0.2)

# Programa principal
def main():
    while True:
        # Leer la humedad del suelo
        humedad_suelo = leer_humedad_suelo()
        print(f"Humedad del suelo: {humedad_suelo}%")

        # Control de la bomba
        if humedad_suelo < UMBRAL_HUMEDAD:
            print("Humedad baja, activando la bomba...")
            bomba.on()  # Encender LED (bomba)
            beep(1)  # Emitir un pitido al encender
            time.sleep(10)  # Simula el riego durante 10 segundos
            bomba.off()  # Apagar LED (bomba)
            beep(2)  # Emitir dos pitidos al apagar
            print("Bomba apagada.")
        else:
            print("Humedad adecuada, la bomba está apagada.")

        # Esperar antes de la próxima lectura
        time.sleep(5)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

