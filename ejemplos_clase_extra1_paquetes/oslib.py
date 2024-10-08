import os

# Listar archivos y directorios en el directorio actual
print(os.listdir('.'))

# Crear un nuevo directorio
os.mkdir('nuevo_directorio')

# Renombrar un archivo o directorio
os.rename('nuevo_directorio', 'directorio_renombrado')

# Eliminar un directorio
os.rmdir('directorio_renombrado')

# Obtener el nombre del sistema operativo
print(os.name)  # 'posix' en Unix, 'nt' en Windows

# Obtener las variables de entorno
print(os.environ)

# Obtener el nombre del usuario actual
print(os.getlogin())