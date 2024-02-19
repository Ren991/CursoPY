# Funcion que encapsula otra funcion
# Mantiene un estado
# La funcion anidada puede acceder a las 
# variables locales definidas en la funcion principal o externa

# Funcion principal 
def operacion(a,b):
    # Definimos una función interna o anidada
    def sumar():
        return a+b
    
    #Retornar la función 
    return sumar


mi_funcion_closure= operacion(5,2)

print(f"Resultado de la funcion closure: {mi_funcion_closure()}")


# Llamar la funcion regresada al vuelo
print(f"Resultado de la función closure al vuelo: {operacion(2,3)()}")


def operacion_lambda(a,b):
    #1. Definimos función lambda interna o anidada y la retornamos
    
    return lambda: a+b

mi_funcion_lamda_closure = operacion_lambda(5,2)
print(f"Resultado de la funcion closure lambda: {mi_funcion_lamda_closure()}")