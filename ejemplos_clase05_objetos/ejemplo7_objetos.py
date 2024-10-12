class Persona():

    # Método constructor
    def __init__(self, cnombre, cedad, ccabello):
        self.nombre = cnombre
        self.edad = cedad
        self.cabello = ccabello

    # Método normal
    def identificarse(self): 
        print(f"Hola. Soy {self.nombre} y tengo {self.edad} años y mi cabello es {self.cabello}.")

persona1 = Persona("Juan", 42, "Rubio") # Instanciamos
persona1.identificarse()