import matplotlib.pyplot as plt

# Datos
datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Crear el histograma
plt.hist(datos, bins=5)

# Añadir título y etiquetas
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()