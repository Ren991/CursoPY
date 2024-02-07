import math
from decimal import Decimal
#Nan - Not a Number(no es un número)
#NaN es un tipo de dato numérico indefinido
a = float("NaN") #=> el valor NaN no es sensible a mayúsuclas

""" print(f"a: {a}")
print(f"Es NaN ?: {math.isnan(a)}") """

a = Decimal("NaN")
print(f"a: {a}")
print(f"Es NaN ?: {math.isnan(a)}")