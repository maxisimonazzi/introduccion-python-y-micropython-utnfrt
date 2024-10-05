def sumar(num1, num2):
    return num1 + num2
def restar(num1, num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return None
    
def calcular(num1, num2, op):
    if op == 1:
        return sumar(num1, num2)
    elif op == 2:
        return restar(num1, num2)
    elif op == 3:
        return multiplicar(num1, num2)
    elif op == 4:
        return dividir(num1, num2)
    else:
        print("Opción incorrecta")
    
# Programa principal
n1 = int(input("\nIngrese un número: "))
n2 = int(input("\nIngrese otro número: "))
op = int(input("\nSeleccione la operación: 1: Sumar; 2: Restar; 3: Multiplicar; 4: Dividir: "))
resultado = calcular(n1, n2, op)
print(f'\nEl resultado es: {resultado}\n')