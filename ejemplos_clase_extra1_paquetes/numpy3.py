import numpy as np

# Crear una matriz
matriz = np.array([[1, 2], [3, 4]])

# Inversa de la matriz
inversa = np.linalg.inv(matriz)
print("Inversa:\n", inversa)

# Determinante de la matriz
determinante = np.linalg.det(matriz)
print("Determinante:", determinante)

# Valores y vectores propios
valores_propios, vectores_propios = np.linalg.eig(matriz)
print("Valores propios:", valores_propios)
print("Vectores propios:\n", vectores_propios)