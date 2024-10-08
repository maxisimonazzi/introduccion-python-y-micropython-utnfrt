def cuadradoDePar(numero):
    if not numero % 2 == 0:
        return
    else:
        return numero ** 2
    
# Programa principal
print(cuadradoDePar(8)) # 64
print(cuadradoDePar(3)) # None, porque no es par