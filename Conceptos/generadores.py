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
        

