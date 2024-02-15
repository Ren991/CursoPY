#Las listas son mutables

nombres1 = ["Juan","Karla","Pedro"]
nombres2 = "Laura María Gonzalo Ernesto".split()

#Sumar listas usando operador +

print(f"Sumar listas {nombres1+nombres2}")
#Extender una lista con otra lista

nombres1.extend(nombres2) # Se le agrega a la lista "nombres1" los elementos de la lista "nombres2"
print(f"Exntender la lista1 {nombres1}")


# Lista numeros
numeros1 = [10,40,15,4,20,90,4]

#Indice del primer elemento
print(f"Indice 4: {numeros1.index(4)}")

#Invertir el orden de los elementos de una lista
numeros1.reverse()
print(numeros1)

#Ordenar los elementos de una lista
numeros1.sort()
print(f"Lista Ordenada: {numeros1}")

#Ordenar de manera desendente
numeros1.sort(reverse=True)
print(f"Lista ordenada(descendente): {numeros1 }")

#Obtener el valor min y max de una lista
print(f"Valor minimo: {min(numeros1)}")
print(f"Valor maximo: {max(numeros1)}")

#Copiar los elementos de una lista // Solo se copia la referencia en memoria.
numeros2 = numeros1.copy()
print(f"Misma referencia ? {numeros1 is numeros2}")#Devuelve False
print(f"Mismo contenido: {numeros1 == numeros2}")#Devuelve True

#Podemos usar el constructor de la lista
numeros2= list(numeros1)
print(f"Misma referencia ? {numeros1 is numeros2}")#Devuelve False
print(f"Mismo contenido: {numeros1 == numeros2}")#Devuelve True

#Otra forma para copiar es usando slicing

numeros2= numeros1[:]
print(f"Misma referencia ? {numeros1 is numeros2}")#Devuelve False
print(f"Mismo contenido: {numeros1 == numeros2}")#Devuelve True

