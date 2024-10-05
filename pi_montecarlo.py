# Calcular pi mediante el metodo de montecarlo

import random

def calcular_pi_mc(num_puntos):
    """
    Calcula el valor de pi mediante el metodo de Monte Carlo. Se debe pasar como argumento el numero de puntos a generar.
    """
    dentro_del_circulo = 0

    for _ in range(num_puntos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distancia = x**2 + y**2

        if distancia <= 1:
            dentro_del_circulo += 1

    pi_aproximado = 4 * (dentro_del_circulo / num_puntos)
    print(pi_aproximado)

# Número de puntos a generar
calcular_pi_mc(1000)