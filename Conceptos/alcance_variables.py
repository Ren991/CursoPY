# Alcance de variables( scope)
# variable declarada fuera de cualquier funcion es una variable globar

var_global = "Variable global"
def imprimir():
    #Acceder a una variable global
    print(f"Variable global desde funcion:{var_global}")

    # Variable local 
    var_local = "Variable local"

    print(f"Variable local desde funcion: {var_local}")

imprimir()
print(f"Var global fuera de la funcion: {var_global}")

#print(f"Variable local fuera funcion: {var_local}")#Devuelve error pq la variable es global y se llama fuera del bloque al que pertenece



