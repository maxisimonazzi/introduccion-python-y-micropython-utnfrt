import matplotlib.pyplot as plt

# Datos
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [5, 7, 3, 8, 4]

# Crear el gráfico
plt.bar(categorias, valores)

# Añadir título y etiquetas
plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()