import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(-10, 10, 400)
y = x**2

# Crear el gráfico
plt.plot(x, y)

# Añadir título y etiquetas
plt.title('Parábola y = x^2')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()