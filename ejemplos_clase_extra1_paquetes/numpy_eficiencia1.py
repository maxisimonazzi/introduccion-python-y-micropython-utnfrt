import numpy as np
import time

# Tamaño del array
tamano = 100000000

# Crear una lista de Python y un array de NumPy con los mismos números
python_list = list(range(tamano))
numpy_array = np.arange(tamano)

# Medir el tiempo de ejecución de la suma en la lista de Python
start_time = time.time()
python_sum = sum(python_list)
end_time = time.time()
python_time = end_time - start_time

# Medir el tiempo de ejecución de la suma en el array de NumPy
start_time = time.time()
numpy_sum = np.sum(numpy_array)
end_time = time.time()
numpy_time = end_time - start_time

# Imprimir los resultados
print(f"Tiempo de ejecución con lista de Python: {python_time:.6f} segundos")
print(f"Tiempo de ejecución con array de NumPy: {numpy_time:.6f} segundos")