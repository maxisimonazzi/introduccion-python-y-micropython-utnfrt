class Persona():
    piernas = 2 # Atributo DE CLASE
    
    def caminar(self): # Definimos un método
        print("Estoy caminando.")

juan = Persona() # Instanciamos un objeto
juan.caminar() # Invocamos el método caminar()