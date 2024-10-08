import numpy as np

# Crear un array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Transponer el array
transpuesta = array.T
print("Transpuesta:\n", transpuesta)

# Redimensionar el array
redimensionado = array.reshape(1, 9)
print("Redimensionado:\n", redimensionado)

# Dividir el array en sub-arrays
sub_arrays = np.split(array, 3)
print("Sub-arrays:", sub_arrays)