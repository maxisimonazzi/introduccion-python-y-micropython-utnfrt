from datetime import datetime, timedelta

# Obtener la fecha y hora actual
fecha_actual = datetime.now()
print("-"*50)
print("Fecha y hora actual:", fecha_actual)
print("-"*50)
# Sumar 5 días a la fecha actual
nueva_fecha = fecha_actual + timedelta(days=5)
print("-"*50)
print("Fecha y hora con 5 dias mas:", nueva_fecha)  # Imprime la nueva fecha
print("-"*50)
# Restar 2 horas a la fecha actual
nueva_fecha = fecha_actual - timedelta(hours=2)
print("-"*50)
print("Fecha y hora, con dos horas menos:", nueva_fecha)  # Imprime la nueva fecha
print("-"*50)