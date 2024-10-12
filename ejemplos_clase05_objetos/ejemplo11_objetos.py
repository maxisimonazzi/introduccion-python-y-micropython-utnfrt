class Alumno: # Creamos la clase
    
    nro_alumnos = 0 # Cantidad de legajos existentes

    # Constructor
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        Alumno.nro_alumnos += 1 # Agregamos un legajo
        print(f"Alumno {self.nombre} dado de alta.")

    # Mostrar datos del objeto
    def __str__(self):
        return f"Nombre: {self.nombre} (nota: {self.nota})"
    
    # Damos de baja el alumno
    def __del__(self):
        Alumno.nro_alumnos -= 1 # Restamos un legajo
        print(f"Alumno {self.nombre} dado de baja.")
        print(f"{Alumno.nro_alumnos} legajos restantes.")

    # Mostrar estado del alumno
    def mostrar_estado(self):
        print(f"El estado de {self.nombre} es ",end="")
        if self.nota <= 4:
            print("regular")
        elif self.nota < 9:
            print("bueno")
        else:
            print("excelente")

# Programa principal
alumno1 = Alumno("Aldo López", 8)
alumno2 = Alumno("Juana Martín", 3)
alumno3 = Alumno("Pedro Gómez", 10)
alumno4 = Alumno("María Pérez", 5)

print(f"Existen {Alumno.nro_alumnos} legajos.")

input("\nPulse enter para continuar\n")

print(alumno1)
print(alumno2)

alumno3.mostrar_estado()
alumno4.mostrar_estado()

input("\nPulse enter para continuar\n")

del alumno2

input("\nPulse enter para continuar\n")

alumno5 = Alumno("Carlos Sánchez", 7)
print(f"Existen {Alumno.nro_alumnos} legajos.")

input("\nPulse enter para continuar\n")