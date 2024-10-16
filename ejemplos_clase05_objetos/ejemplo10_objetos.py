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
        print(f"Se ha eliminado el objeto {self.nombre}.")


persona1 = Persona("Juan", 42, "Rubio") # Instanciamos
print(persona1)