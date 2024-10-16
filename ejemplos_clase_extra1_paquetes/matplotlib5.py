import matplotlib.pyplot as plt

# Datos
etiquetas = ['A', 'B', 'C', 'D']
tamaños = [15, 30, 45, 10]

# Crear el gráfico de tarta
plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%')
plt.title('Gráfico de Tarta')
plt.show()