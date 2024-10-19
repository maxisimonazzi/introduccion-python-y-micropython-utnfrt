import time

def calcular_pi_lb(iteraciones):
    """
    Calcula el valor de pi mediante el metodo de Leibniz. Se dene pasar como argumento el numero de iteraciones.    
    """
    # Valor de K
    k = 1.0
    
    # Inicializamos la suma
    s = 0.0
    
    for i in range(iteraciones):
    
        # elementos con indice par son positivos
        if i % 2 == 0:
            s += 4/k
        else:
            # elementos con indice impar son negativos
            s -= 4/k
    
        k += 2
        
    print(s)

inicio = time.ticks_ms()
calcular_pi_lb(500000)
fin = time.ticks_ms()

tiempo_transcurrido = fin - inicio
print("Tiempo de ejecución:", tiempo_transcurrido, "ms")