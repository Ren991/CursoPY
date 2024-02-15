# Profundizando en tuplas

#Declarar variables
a, b =" Hola","Adios"
print(a,b)

#swap (intercambio de variables
a,b = b,a
print(a,b)

# Regeresar multiples valores en una funcion

def minmax(elementos):
    return min(elementos), max(elementos)

min,max = minmax([1,2,3,4,5])

print(f"Valor min:{min}, valor max: {max}" )

# Regresa la suma de una tupla

resultado = sum((1,2,3,4,5))
print(f"Resultado: {resultado}")

def sumar(*args): #=> Los argumentos se transforman en una tupla 
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(f"Resultado con funcion: {resultado}")