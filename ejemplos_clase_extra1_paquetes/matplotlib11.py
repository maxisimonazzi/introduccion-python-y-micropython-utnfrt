import matplotlib.pyplot as plt
import numpy as np

# Generar las señales
x = np.linspace(0, 10, 1000)
y1 = np.sin(x)  # Calcular el seno de cada punto
y2 = np.cos(x)  # Calcular el coseno de cada punto
y3 = np.tan(x)  # Calcular el cuadrado de cada punto

# Crear los gráficos
plt.figure(figsize=(12, 8))

# Gráfico de la primera señal
plt.subplot(3, 1, 1)
plt.plot(x, y1)
plt.title('Señal 1: Seno')

# Gráfico de la segunda señal
plt.subplot(3, 1, 2)
plt.plot(x, y2)
plt.title('Señal 2: Coseno')

# Gráfico de la convolución
plt.subplot(3, 1, 3)
plt.plot(x, y3)
plt.title('Señal 3: Tangente')
plt.ylim(-100, 100)

# Mostrar los gráficos
plt.tight_layout()
plt.show()