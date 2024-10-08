import numpy as np
import time

# Tamaño de las matrices
size = 500

# Crear matrices de Python y NumPy con números aleatorios
python_matrix_a = [[np.random.rand() for _ in range(size)] for _ in range(size)]
python_matrix_b = [[np.random.rand() for _ in range(size)] for _ in range(size)]
numpy_matrix_a = np.random.rand(size, size)
numpy_matrix_b = np.random.rand(size, size)

# Función para multiplicar matrices usando listas de Python
def python_matrix_multiply(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

# Medir el tiempo de ejecución de la multiplicación de matrices en listas de Python
start_time = time.time()
python_result = python_matrix_multiply(python_matrix_a, python_matrix_b)
end_time = time.time()
python_time = end_time - start_time

# Medir el tiempo de ejecución de la multiplicación de matrices en arrays de NumPy
start_time = time.time()
numpy_result = np.dot(numpy_matrix_a, numpy_matrix_b)
end_time = time.time()
numpy_time = end_time - start_time

# Imprimir los resultados
print(f"Tiempo de ejecución con matrices de Python: {python_time:.6f} segundos")
print(f"Tiempo de ejecución con matrices de NumPy: {numpy_time:.6f} segundos")