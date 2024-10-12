class Persona():
    moviendo = False 

    def caminar(self):
        self.moviendo = True

    def detener(self):
        self.moviendo = False

juan = Persona()

juan.caminar()
print(juan.moviendo) # True

juan.detener()
print(juan.moviendo) # False