import matplotlib.pyplot as plt
import numpy as np

# Datos
datos = [np.random.rand(50), np.random.rand(50), np.random.rand(50)]

# Crear el gráfico de caja
plt.boxplot(datos)
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Caja')
plt.show()