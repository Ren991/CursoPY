#Las funciones lambda son funciones anónimas, además son funciones pequeñas
# Solo una linea de código

#No es posible asignar una función a una variable
# mi_funcion = def sumar(a,b): return a+b

# No se necesita agregar paréntesis para los parámetros en funciones lambda
# ""        ""   palabra return

mi_funcion_lambda = lambda a,b: a+b

resultado = mi_funcion_lambda(4,6)
print(f" Resultado de sumar con funcion lambda: {resultado}")

# Funcion lambda que no recibe argumentos( debemos regresar expresion válida):

mi_funcion_lambda = lambda: "Funcion sin argumentos"

print(f"Llamar funcion lambda sin argumentos: { mi_funcion_lambda()}")

# Funcion lambda con parámetros por default

mi_funcion_lambda = lambda a=2,b=3: a +b 

print(f"Resultado argumentos por default: {mi_funcion_lambda()}")


# Función lambda con argumentos variables con *args y **kwargs

mi_funcion_lambda = lambda *args, **kwargs: len(args)+ len(kwargs)

print(f"resultado argumentos variables: {mi_funcion_lambda(1,2,3,a =5,b=6)}")

# Funciones lambda con argumentos, argumentos variables y valores por default

mi_funcion_lambda = lambda a,b ,c=3 , *args,**kwargs: a+b+c+len(args)+len(kwargs)

print(f"Resultado funcion lambda: {mi_funcion_lambda(1,2,4, 5,6,7,e=5,f=7)}")