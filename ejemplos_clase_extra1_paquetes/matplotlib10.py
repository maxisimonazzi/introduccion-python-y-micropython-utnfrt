import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 2 * np.pi, 1000)  # Generar 1000 puntos entre 0 y 2π
y1 = np.sin(x)  # Calcular el seno de cada punto
y2 = np.cos(x)  # Calcular el coseno de cada punto
y3 = np.tan(x)  # Calcular el cuadrado de cada punto

# Crear el gráfico
plt.plot(x, y1, label='Seno')
plt.plot(x, y2, label='Coseno')
plt.plot(x, y3, label='Tangente')

# Añadir título y etiquetas
plt.title('Onda Senoidal y Cosenoidal')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Especificar los límites del eje y
plt.ylim(-3, 3)

# Añadir una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()