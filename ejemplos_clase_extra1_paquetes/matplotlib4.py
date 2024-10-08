import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.random.rand(50)
y = np.random.rand(50)

# Crear el gráfico de dispersión
plt.scatter(x, y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Dispersión')
plt.show()