class Persona:
    piernas = 2

juan = Persona()
manuel = Persona()

# Imprimimos un atributo del objeto
print(juan.piernas) # 2
print(manuel.piernas) # 2

# Atributo de instancia
juan.edad = 34
manuel.edad = 26

print(juan.edad) # 34
print(manuel.edad) # 26