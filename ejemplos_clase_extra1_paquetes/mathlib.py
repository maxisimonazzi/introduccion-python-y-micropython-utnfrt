import math

print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

angulo = math.radians(30)  # Convertir grados a radianes
print(math.sin(angulo))  # 0.49999999999999994
print(math.cos(angulo))  # 0.8660254037844387
print(math.tan(angulo))  # 0.5773502691896257
print(math.degrees((math.pi)/2)) # 90.0 (convertir radianes a grados)

print(math.exp(1))  # 2.718281828459045
print(math.log(10))  # 2.302585092994046 (logaritmo natural)
print(math.log10(100))  # 2.0 (logaritmo base 10)
print(math.log(100, 10)) # 2.0 (logaritmo base 10)
print(math.pow(2, 3))  # 8.0 (2 elevado a la 3)
print(math.sqrt(16))  # 4.0 (raíz cuadrada)

print(math.ceil(4.2))  # 5 (redondeo hacia arriba)
print(math.floor(4.8))  # 4 (redondeo hacia abajo)
print(math.trunc(4.8))  # 4 (truncamiento)
print(math.fabs(-4.8))  # 4.8 (valor absoluto)

print(math.factorial(5))  # 120 (5!)
print(math.comb(5, 2))  # 10 (combinaciones de 5 elementos tomados de 2 en 2)
print(math.perm(5, 2))  # 20 (permutaciones de 5 elementos tomados de 2 en 2)

numeros = [0.9999999, 1, 2, 3]
print(math.fsum(numeros)) # 6.9999999

print(math.gcd(12, 34)) # Máximo común divisor
print(math.lcm(12, 34)) # Mínimo común múltiplo

print((3+4j) * (7+10j))  # (-19+58j) (producto de dos números complejos)
print((3+4j) / (7+10j))  # (0.4117647058823529-0.058823529411764705j) (división de dos números complejos)
print((3+4j) + (7+10j))  # (10+14j) (suma de dos números complejos)
print((3+4j) - (7+10j))  # (-4-6j) (resta de dos números complejos)