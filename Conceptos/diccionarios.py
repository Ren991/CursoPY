# Clave valor
# Los diccionarios guardan un orden (a diferencia de un set)

diccionario = {"Nombre":"Juan", "Apellido":"Perez","Edad":28}

#Los dic son mutables, pero las llaves deben ser inmutables
#diccionario = {[1,2]:"Valor1"} # Esto devuelve error
#diccionario = {(1,2): "Valor1"}# Permite tupla como clave pq la tupla es inmutable
print(diccionario)

# Se agrega una llave si no se encuentra dentro del diccionario

diccionario["Departamento"] = "Sistemas" # Se agrega la llave y el valor sino se encuentra, y si se encuentra reemplaza el valor
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario, la llave es única. 
diccionario["Nombre"] = "Juan carlos"
print(diccionario)

# Recuperar un valor indicando una llave 
print(diccionario["Nombre"])
# Si no encuentra la llave lanza una excepcion
#print(diccionario["nombre"])

#Metodo get recupera una llave y si no existe no lanza una excepcion
# Podemos regresar un valor en caso de que no exista la lalve

print(diccionario.get("Nombres","No se encontró la llave"))
print(diccionario)

# setdefault si modifica el diccionario, ademas se agrega un valor por default

nombre = diccionario.setdefault("Nombress","Valor por default")
print(nombre)

# Imprimir con pprint
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)