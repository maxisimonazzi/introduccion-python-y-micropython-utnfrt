##########################################
#             Importaciones              #
##########################################

from machine import Pin, PWM
from time import sleep_ms
import random

##########################################
#          Definicion de pines           #
##########################################

# Defino pines de los LEDs y botones
led_pins = [
    Pin(14, Pin.OUT),
    Pin(27, Pin.OUT),
    Pin(26, Pin.OUT),
    Pin(25, Pin.OUT)
    ]
boton_pins = [
    Pin(15, Pin.IN, Pin.PULL_UP),
    Pin(4, Pin.IN, Pin.PULL_UP),
    Pin(5, Pin.IN, Pin.PULL_UP),
    Pin(18, Pin.IN, Pin.PULL_UP)
    ]

# Defino pin del speaker (PWM)
speaker_pin = PWM(Pin(23))

# Silencio el speaker
speaker_pin.duty(0)


##########################################
#        Definicion de funciones         #
##########################################

# Función para reproducir un tono
def tono(frecuencia, duracion_ms):
    speaker_pin.freq(frecuencia)
    speaker_pin.duty(50)  # 50% de ciclo de trabajo
    sleep_ms(duracion_ms)
    speaker_pin.duty(0)  # Apagar sonido

# Función para iluminar un LED y reproducir un tono
def iluminar_led(index, frecuencia, duracion_ms):
    led_pins[index].on()
    tono(frecuencia, duracion_ms)

    # Esperar a que el botón se suelte
    while not boton_pins[index].value():
        sleep_ms(50)
    
    led_pins[index].off()
    sleep_ms(300-(dificultad*50))

# Funcion para reproducir la secuencia generada
def reproducir_secuencia():
    for paso in secuencia:
        iluminar_led(paso, tonos[paso], 350-(dificultad*50))
        sleep_ms(350-(dificultad*50))  # Pausa entre pasos

# Funcion para leer el botón presionado
def leer_boton():
    while True:
        for index, boton in enumerate(boton_pins):
            if not boton.value():  # Botón presionado
                iluminar_led(index, tonos[index], 350-(dificultad*50))  # Iluminar y reproducir el tono del botón
                return index
        sleep_ms(50)

# Funcion para verificar si la entrada del jugador es correcta
def verificar_entrada():
    for i in range(len(secuencia)):
        entrada_jugador = leer_boton()
        if entrada_jugador != secuencia[i]:
            return False  # Error en la secuencia
    return True  # Secuencia correcta

##########################################
#     Definicion de tonos y sonidos      #
##########################################

# Tonos asociados a cada botón (frecuencias en Hz)
tonos = [500, 600, 700, 800]

# Reproducir sonido de avance de nivel
def sonido_avance_nivel():
    notas_avance = [330, 392, 523, 262, 294, 784]
    for tone in notas_avance:
        tono(tone, 150)
    speaker_pin.duty(0)  # Apagar sonido

# Reproducir sonido de game over
def sonido_game_over():
    notas_game_over = [(622,300), (587,300), (554,300)]
    for nota, duration in notas_game_over:
        tono(nota, duration)
        sleep_ms(50)
    for _ in range(10):
        for pitch in range(-10, 11):  # Recorrer tonos alrededor de 523
            tono(523 + pitch, 5)
    speaker_pin.duty(0)  # Apagar sonido

# Reproducir de victoria
def sonido_victoria():
    notas_victoria = [
        (196, 100), (262, 100), (330, 100), (392, 100), (523, 100), (659, 100),
         (784, 500), (659, 500), (165, 100), (262, 100), (311, 100), (415, 100),
         (523, 100), (622, 100), (831, 500), (622, 500), (233, 100), (294, 100),
         (349, 100), (466, 100), (587, 100), (689, 100), (932, 500), (932, 100),
         (932, 100), (932, 100), (1047, 500)
         ]
    for nota, duration in notas_victoria:
        tono(nota, duration)
        sleep_ms(50)
        
##########################################
#    Comienzo del programa principal     #
##########################################

random.seed()  # Inicializar el generador aleatorio

# Datos del juego
nivel_maximo = 25
nivel_actual = 0
dificultad = 1
secuencia = []

while True:
    # Añadir un nuevo paso aleatorio a la secuencia
    secuencia.append(random.randint(0, 3))

    # Incremento en 1 el contador de nivel
    nivel_actual += 1

    # Calculo la dificultad en base al nivel
    dificultad = (nivel_actual // 5) + 1

    # Mostrar la secuencia al jugador
    reproducir_secuencia()

    # Verificar la respuesta del jugador
    if not verificar_entrada():
        sonido_game_over()
        nivel_actual = 0
        secuencia = []
        sleep_ms(1000)
    else:
        if nivel_actual < nivel_maximo:
            sonido_avance_nivel()
            sleep_ms(1000)
        else:
            sonido_victoria()
            nivel_actual = 0
            secuencia = []
            sleep_ms(2000)