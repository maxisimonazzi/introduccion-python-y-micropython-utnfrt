import matplotlib.pyplot as plt
import numpy as np

# Datos
datos = np.random.rand(10, 10)

# Crear el gráfico de calor
plt.imshow(datos, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Gráfico de Calor')
plt.show()