from datetime import datetime

fecha = datetime.now() # Fecha y hora actual

print("-"*50)
print("Fecha y hora actual:", fecha) # Imprime fecha y hora actual
print("-"*50)
print("Año:", fecha.year) # Año
print("Mes:", fecha.month) # Mes
print("Dia:", fecha.day) # Dia
print("Hora:", fecha.hour) # Hora
print("Minuto:", fecha.minute) # Minuto
print("Segundo:", fecha.second) # Segundo
print("Microsegundo:", fecha.microsecond) # Microsegundo
print("-"*50)
print(fecha.strftime("%Y-%m-%d -- %H:%M:%S"))