import time
import numpy as np

# Tamaño del array
tamano = 100000000

# Medición para lista de Python
inicio_lista = time.time()
lista = list(range(1, tamano))  # Generar la lista
lista_doble = [x * 2 for x in lista]  # Multiplicar por 2
fin_lista = time.time()

# Mostrar tiempo para lista
print(f"Tiempo con lista de Python: {fin_lista - inicio_lista} segundos")

# Medición para array de NumPy
inicio_array = time.time()
array = np.arange(1, tamano)  # Generar el array
array_doble = array * 2  # Multiplicar por 2
fin_array = time.time()

# Mostrar tiempo para array
print(f"Tiempo con array de NumPy: {fin_array - inicio_array} segundos")