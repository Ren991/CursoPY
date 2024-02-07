# Profundizando en el tipo str 

#help(str) => Devuelve información sobre la clase string.
# la función help da información sobre cualquier cosa.

'''
Comentario varias lineas
'''

mensaje1 = "hola mundo"
mensaje2 = mensaje1.capitalize()

#Las cadenas son inmutables
#Si se sobreescribe una variable el valor de la misma va a almacenarse en otra direccion de memoria.
#Diferente a la de su origen

print(f"Mensaje1: {mensaje1}, id: {hex(id(mensaje1))}") #id() => PAra saber la dirección de memoria a la que pertenece.
print(f"Mensaje2: {mensaje2}, id: {hex(id(mensaje2))}") 

