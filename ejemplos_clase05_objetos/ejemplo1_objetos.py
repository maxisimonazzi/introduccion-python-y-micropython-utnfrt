# Definimos la clase Persona
class Persona:
    # Atributo, presente en todos los objetos que pertenecen a la clase
    piernas = 2

# Instanciamos un objeto de la clase Persona
juan = Persona()

# Imprimimos un atributo del objeto
print(juan.piernas) # 2
print()
print(f"Juan tiene {juan.piernas} piernas.")

# Atributo de instancia
juan.edad = 34
print(juan.edad) # 34
print()
print(f"Juan tiene {juan.edad} años.")