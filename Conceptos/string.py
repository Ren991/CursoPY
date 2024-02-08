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

#Dar formato a un str
nombre ="Juan"
edad = 28

mensaje_con_formato = "Mi nombre es %s y tengo %d años"%(nombre,edad)
""" print(mensaje_con_formato) """

persona = ("Karla","Gomez",5000.00)
#mensaje_con_formato = "Hola %s %s. Tu sueldo es %.2f"%persona
mensaje_con_formato = "Hola %s %s. Tu sueldo es %.2f"
#Los parámetros se pueden poner en la variable o en el print.
print(mensaje_con_formato%persona)

#Método format
name = "Juan"
age = 28
salary = 3000
message_format = "Nombre {} Edad {} Sueldo {:.2f}".format(name,age,salary) 
print(message_format)

#Template str - f str

nombre1 = "Juan"
edad1 = 28
sueldo1 = 3000

mensaje1 = f"Nombre: {nombre1} Edad: {edad1} sueldo: {sueldo1:.2f}"
print(mensaje1)
print(nombre1,edad1, sueldo1, sep=",")#=> El parámetro sep , separa los elementos en ese caso con una ",".

#Multiplicacion de str

resultado = 5*"Hola"
print(f"Resultado: {resultado}")

#Multiplicacion tupla
resultado= 5*("hola","Mundo")
print(f"Resultado: {resultado}")

#Multiplicacion lista

resultado = 10*[0]
print(f"Resultado: {resultado}, largo: {len(resultado)}")

#Caracteres unicode
print("Hola\u0020Mundo") #=> Espacio en blanco
print("Notación simple:","\u0041") #=> Letra A
print("Notación extendida:" , "\U00000041")#=> Letra A
print("Notación haexadecimal","\x41")#=>Letra A
print("Corazon", "\u2665")#=> Corazón
print("Cara sonriendo:", "\U0001f600")# => Cara sonriendo
print("Serpiente:","\U0001F40D")#=> Serpiente

# Caracteres ASCII
caracter = chr(65)
print("A Mayúscula:", caracter)#=> Letra A en código ASCII
caracter = chr(64)
print("Símbolo @:",caracter)#=> Símbolo arroba en códgo ASCII