
a = 3.0
print(f"a: {a:.2f}") #=> muestra 2 decimales dsp de la coma

# Construcctor float pued recibir int y str

a = float(10)
a = float("10")
#print(f"a: {a:.2f}")

#Notacion exponencial (valores positivos o negativos)

a = 3e-5
print(f"a: {a:.5f}")

#Cualquier cálculo que involucre un float, se promueve a float

a = 4.0 +5 
print(a)
print(type(a))

# Manejo de valores infitos. Existe un valor negativo infinito y un valor positivo infinito.

import math #=> libreria math contiene un módulo para saber si un float es infinito
from decimal import Decimal

infinito_positivo = float("inf")
""" print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}") """

infinito_negativo = float("-inf")
""" print(f"infinito negativo: {infinito_negativo}")
print(f"Es infinito negativo: {math.isinf(infinito_negativo)}") """

infinito_positivo = math.inf

""" print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}") """

infinito_negativo = -math.inf

""" print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito: {math.isinf(infinito_negativo)}") """

#Modulo decimal 
infinito_positivo = Decimal("Infinity")
print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}")

infinito_negativo = Decimal("-Infinity")
print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito: {math.isinf(infinito_negativo)}")
