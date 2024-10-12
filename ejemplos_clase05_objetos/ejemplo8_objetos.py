class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return self.lado * 4
    
cuad1 = Cuadrado(15)
print(f"El area del cuadrado es {cuad1.calcular_area()}") 
print(f"El perimetro del cuadrado es {cuad1.calcular_perimetro()}")

cuad1.lado = 12
print(f"La nueva area del cuadrado es {cuad1.calcular_area()}") 
print(f"El nuevo perimetro del cuadrado es {cuad1.calcular_perimetro()}")