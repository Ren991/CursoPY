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

#Método join

tupla_str = ("hola","mundo", "como","estas")
mensaje = " ".join(tupla_str)
print(f"Mensaje: {mensaje}")

lista_cursos = ["Java","Python", "Angular", "Spring"]
mensaje = ", ".join(lista_cursos)

print(lista_cursos)

cadena = "HolaMundo"
mensaje = ".".join(cadena)
print(f"Mensaje: {mensaje}")

diccionario = {"Nombre":"juan", "apellido":"Perez","edad":"18"}

llaves = "-".join(diccionario.keys())
valores = "-".join(diccionario.values())

print(f"Llaves:{llaves} , type:{type(llaves)}")
print(f"valores:{valores} , type: {type(valores)}")

#Método split = dividir una cadena delimitada en subcadenas

cursos = "Java Python Javascript Angular Spring Excel"
lista_cursos = cursos.split()
print(f"Lista cursos: {lista_cursos}")

cursos = "Java , Python , Javascript , Angular , Spring , Excel"
lista_cursos = cursos.split(" , ",3)#=> con el segundo parámetro los primeros tres elementos se separan y el resto queda en una cadena.
print(f"Lista cursos: {lista_cursos}")