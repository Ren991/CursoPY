# Generador Es funcion especial en py 
# Permite regresar secuencia de valores
# Suspende la ejecució de la funcion yield (producir)
# No se usa return

#CLASE GENERATOR

def generador():
    yield 1
    print("Se reanuda la ejecución")
    yield 2
    print("Se reanuda la ejecución")
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor

print(next(gen))
print(next(gen))
print(next(gen))

# Si tratamos de consumir mas valores de los que produce el generador
# lanza un error

for valor in generador():
    print(f"Numero generado: {valor}")
    
# Ejemplos de generadores

# Generador de numeros del 1 al 5 
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print("Se reanuda la ejecución")
        
generador = generador_numeros()

# Consumimos los valores del generador

for valor in generador:
    print(f"Numero producido por el generador: {valor}")
        

# Expresiones GENERADORAS ( es un generador anónimo)

multiplicacion = (valor*valor for valor in range(4))
#                 se aplica la  |=> For normal
#                 multiplicación|            

print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

# Expresión generadora a una función ( sin paréntesis)

import math

suma = sum(valor * valor for valor in range(4))
print(f"Resultado suma: {suma}")

# También se puede usar una lista 
# o cualquier otro iterador

lista = ["Juan","Perez"]
generador = (valor for valor in lista)

print(next(generador))
print(next(generador))

# Crear un string a partir de un generador
# Creado a partir de una lista

lista = ["Karla","Gomez"]

contador = 0
# incrementar contador
def incrementar():
    global contador
    contador += 1
    return contador

# La primera parte es el yield de nuestro generador
# La segunda parte es el for

generador_inc = (f"{incrementar()}. {nombre}" for nombre in lista)

lista = list(generador_inc)
print(lista)


