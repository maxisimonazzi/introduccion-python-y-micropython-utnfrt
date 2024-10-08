import numpy as np

# Generar 10 números equiespaciados entre 0 y 1
array_linspace = np.linspace(0, 1, 10)
print("Linspace:", array_linspace)

# Generar 5 números equiespaciados entre 0 y 10, incluyendo el endpoint
array_linspace_incl = np.linspace(0, 10, 5, endpoint=True)
print("Linspace (incluyendo endpoint):", array_linspace_incl)

# Generar 5 números equiespaciados entre 0 y 10, excluyendo el endpoint
array_linspace_excl = np.linspace(0, 10, 5, endpoint=False)
print("Linspace (excluyendo endpoint):", array_linspace_excl)

# Generar números desde 0 hasta 10 con un paso de 2
array_arange = np.arange(0, 10, 2)
print("Arange:", array_arange)

# Generar números desde 1 hasta 10 con un paso de 0.5
array_arange_float = np.arange(1, 10, 0.5)
print("Arange (con paso flotante):", array_arange_float)

# Generar 10 números equiespaciados en una escala logarítmica entre 10^0 y 10^2
array_logspace = np.logspace(0, 2, 10)
print("Logspace:", array_logspace)

# Generar 5 números equiespaciados en una escala logarítmica entre 10^1 y 10^3
array_logspace_custom = np.logspace(1, 3, 5)
print("Logspace (custom):", array_logspace_custom)