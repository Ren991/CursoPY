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

#Multiplicacion listas

lista_multiplicacion = 5*[[2, 5]]
print(lista_multiplicacion)

lista_multiplicacion[2].append(10) #=> Apendea un 10 a todas las listas.
print(lista_multiplicacion)

#Matrices en python

matriz = [[10,20],[30,40,50],[60,70,80,90]]
print(f"Matriz original: {matriz}")

print(f"Recuperar Renglon 0 columna 0: {matriz[0][0]}")
print(f"Recuperar Renglon 2 columna 2: {matriz[2][2]}")

#Modificar valor en matriz
matriz[2][0] = 65
print(f"Matriz modificada{matriz}")