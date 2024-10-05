def obtenerDescuento(precio, porcentaje):
    descuento = precio * porcentaje/100
    precioNuevo = precio - descuento
    print()
    print(f'Precio original: ${precio:.2f}')
    print(f'Descuento: $ {descuento:.2f}')
    print(f'Precio nuevo: $ {precioNuevo:.2f}')
    print()

# Programa principal
print()
precio_original = int(input("Ingrese el valor original del producto: "))
descuento = int(input("Ingrese el descuento que quiere aplicar: "))
obtenerDescuento(precio_original, descuento)