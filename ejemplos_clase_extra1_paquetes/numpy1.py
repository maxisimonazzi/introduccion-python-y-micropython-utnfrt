import numpy as np

# Crear un array unidimensional
array_1d = np.array([1, 2, 3, 4, 5])
print("Array 1D:", array_1d)

# Crear un array bidimensional
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:\n", array_2d)

# Crear un array de ceros
array_ceros = np.zeros((3, 3))
print("Array de ceros:\n", array_ceros)

# Crear un array de unos
array_unos = np.ones((2, 4))
print("Array de unos:\n", array_unos)

# Crear un array con valores aleatorios
array_aleatorio = np.random.random((2, 2))
print("Array aleatorio:\n", array_aleatorio)