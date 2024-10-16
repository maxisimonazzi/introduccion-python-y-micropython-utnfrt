class Persona():

    # Método constructor
    def __init__(self, cnombre, cedad, ccabello):
        self.nombre = cnombre
        self.edad = cedad
        self.cabello = ccabello

    # Método str
    def __str__(self): 
        return f"Hola. Soy {self.nombre} y tengo {self.edad} años y mi cabello es {self.cabello}."
    
    # Método del
    def __del__(self):
        print(f"Se ha eliminado al a persona {self.nombre}.")

    # Método normal
    def mostrar_nombre(self):
        print(f"Mi nombre es {self.nombre}. Yo soy un metodo de la superclase Persona.")

class empleado(Persona):

    # Método constructor
    def __init__(self, cnombre, cedad, ccabello, csalario):
        self.nombre = cnombre
        self.edad = cedad
        self.cabello = ccabello
        self.salario = csalario

    # Método normal
    def mostrar_salario(self):
        print(f"Mi salario es {self.salario}.")
    
    # Método del
    def __del__(self):
        print(f"Se ha eliminado el empleado {self.nombre}.")

# Crear un objeto de la clase Empleado
empleado1 = empleado("Carlos", 28, "Negro", 50000)
print(empleado1)
empleado1.mostrar_nombre()