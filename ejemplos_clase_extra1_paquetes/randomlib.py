import random

# Generar un número flotante aleatorio entre 0 y 1
print(random.random())

# Generar un número flotante aleatorio entre 1 y 10
print(random.uniform(1, 10))

# Generar un número entero aleatorio entre 1 y 10
print(random.randint(1, 10))

# Generar un número entero aleatorio de 0 a 9, 10 excluído
print(random.randrange(10))

# Entero aleatorio de 0 a 100
print(random.randrange(0,101))

# Entero aleatorio de 0 a 100 cada 2 números, múltiplos de 2
print(random.randrange(0,101,2))

# Entero aleatorio de 0 a 100 cada 5 números, múltiplos de 5
print(random.randrange(0,101,5))

# Seleccionar un elemento aleatorio de una cadena
print(random.choice("Introduccion a Python y Micropython"))

# Seleccionar un elemento aleatorio de una lista
print(random.choice(['Manzana', 'Banana', 'Pera', 'Uva', 'Naranja']))

# Seleccionar múltiples elementos aleatorios de una lista con reemplazo
print(random.choices(['Manzana', 'Banana', 'Pera', 'Uva', 'Naranja'], k=4))

# Seleccionar múltiples elementos aleatorios de una lista sin reemplazo
print(random.sample(['Manzana', 'Banana', 'Pera', 'Uva', 'Naranja'], k=4))

# Reordenar aleatoriamente los elementos de una lista
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)

# Establecer una semilla para obtener resultados reproducibles
random.seed(42)
print(random.randint(1, 10))  # Siempre imprimirá el mismo número
print(random.random())  # Siempre imprimirá el mismo número