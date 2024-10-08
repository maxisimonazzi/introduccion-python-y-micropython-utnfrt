def generarMail(nombre, apellido, anio):
    print()
    mail = f"Tu email es: {nombre[0].lower()}{apellido.lower()}{anio}@gmail.com"
    print()
    print(mail)
    print()

# Programa principal
print()
a = input("Ingrese su nombre: ")
b = input("Ingrese su apellido: ")
c = int(input("Ingrese su año de nacimiento: "))
generarMail(a, b, c)