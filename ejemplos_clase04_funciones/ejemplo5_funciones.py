#Calcula e imprime la raíz de un número dado.
# num: El número del cual se va a calcular la raíz.
# raiz (opcional): El grado de la raíz. Por defecto es 2 (raíz cuadrada).

def fnRaiz(num, raiz=2):
    print(num**(1/raiz))

fnRaiz(9)		# 3
fnRaiz(8)		# 2,8284
fnRaiz(8,3)	    # 2
