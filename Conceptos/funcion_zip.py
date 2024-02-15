print(dir(__builtins__))

numeros = (1,2,3)
letras = ["a","b","c"]
identificadores = 321,322,323,324,325
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros,letras,identificadores,conjunto)
print(mezcla)#=> Objeto de tipo zip

print(list(mezcla))#=> Lista que en cada indice tiene una tupla con un numero y una letra.
print(tuple(zip(numeros,letras)))#=> Tupla de tuplas

#Iterar en paralelo

for numero,letra,id,aleatorio in zip(numeros,letras,identificadores,conjunto):
    print(f"Numero: {numero}, Letra: {letra} , Id: {id}, aleatorio: {aleatorio}")
    
nueva_lista = []

for numero, letra,id,aleatorio in zip (numeros,letras,identificadores,conjunto):
    nueva_lista.append(f"{id}-{numero}-{letra}-{aleatorio}")
print(nueva_lista)

# unzip => Separa iterables

mezcla = [(1,"a"),(2,"b"),(3,"c")]
numeros,letras = zip(*mezcla) #=> Desempaqueta numeros y letras
print(f"Numeros: {numeros}")
print(f"Letras: {letras}")

# ordenamiento usando zip

letras = ["c","d","a","e","b"]
numeros = [3,2,4,1,0]

mezcla= zip(letras,numeros)
#sin orden
print(tuple(mezcla))
#con orden
print(sorted(zip(numeros,letras)))#=> primer parámetro del método zip determina el orden

# Crear un diccionario con zip y dos iterables

llaves = ["Nombre","apellido","Edad"]
valores = ["Juan", "perez",18]

diccionario = dict(zip(llaves,valores))
print(diccionario)

# Actualizar un elemento de un diccionario

llave= ["Edad"]
nueva_edad = [28]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)