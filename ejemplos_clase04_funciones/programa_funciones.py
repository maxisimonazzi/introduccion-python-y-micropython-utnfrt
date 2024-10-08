def saludar():
    print()
    print("Bienvenidos a la Universidad! UTN-FRT")
    print("-"*37)
    print()

def mostrar_horario_mañana():
    print()
    print("El horario del turno de la mañana es de 08 a 12 horas")
    print()
def mostrar_horario_tarde():
    print()
    print("El horario del turno de la tarde es de 14 a 18 horas")
    print()
def mostrar_horario_noche():
    print()
    print("El horario del turno de la noche es de 19 a 23 horas")
    print()
def mostrar_menu():
    print("Bienvenidos a la Universidad! ¿Qué horarios desea consultar?: ")
    print()
    print("1. Mañana")
    print("2. Tarde")
    print("3. Noche")
    print()

saludar()
mostrar_menu()
opcion_elegida = int(input("Elige una opción (1, 2 o 3): "))
if opcion_elegida == 1:
    mostrar_horario_mañana()
elif opcion_elegida == 2:
    mostrar_horario_tarde()
elif opcion_elegida == 3:
    mostrar_horario_noche()
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")