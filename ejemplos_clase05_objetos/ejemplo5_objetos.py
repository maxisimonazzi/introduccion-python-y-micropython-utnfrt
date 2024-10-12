class Persona():
    moviendo = False 

    def caminar(self):
        self.moviendo = True

    def detener(self):
        self.moviendo = False

juan = Persona()
manuel = Persona()

juan.caminar()
print(juan.moviendo) # True

manuel.caminar()
print(manuel.moviendo) # True

juan.detener()
print(juan.moviendo) # False
print(manuel.moviendo) # True