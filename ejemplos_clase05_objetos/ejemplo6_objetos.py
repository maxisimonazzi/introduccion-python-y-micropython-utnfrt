class Persona():

    # Método constructor
    def constructor(self, cnombre, cedad, ccabello):
        self.nombre = cnombre
        self.edad = cedad
        self.cabello = ccabello

    def identificarse(self): # Método normal
        print(f"Hola. Soy {self.nombre} y tengo {self.edad} años y mi cabello es {self.cabello}.")

persona1 = Persona() # Instanciamos
persona1.constructor("Juan", 42, "Rubio")
persona1.identificarse()