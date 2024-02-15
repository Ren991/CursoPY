#Unpacking significa desempaquetado. permite asignar los elementos de una secuencia a variables individuales

valores = 1,2,3 # => se crea una tupla
print(valores)
print(type(valores))

valor1,valor2,valor3 = 1,2,3
print(valor1,valor2,valor3)

valor1,_,valor3 = 1,2,3 #=> "_" es una convención para no tener en cuenta el segundo valor

valor1,valor2,*valor3 = 1,2,3,4,5,6,7,8,9 # el * hace que en la variable valor 3 se almacen todos los valores restantes
print(valor1,valor2,valor3)

valor1,valor2,*valor3,valor4,valor5 = 1,2,3,4,5,6,7,8,9
# En este caso valor1=1 , valor2=2 ,valor4=8, valor5=9 y el resto es valor3



def obtener_coordenadas():
    # Esta función devuelve una tupla con dos valores
    return 3, 4

# Llamamos a la función y desempaquetamos el resultado en dos variables
x, y = obtener_coordenadas()

# Imprimimos las coordenadas obtenidas
print("Coordenada x:", x)
print("Coordenada y:", y)

numeros = [1,2,3]
print(*numeros, sep=" - ")#Desempaquetando cada elemento

def sumar(a,b,c):
    print(f"Resultado suma: {a+b+c}")
    
sumar(*numeros) # => Se desempaqueta el array numeros para que pase como 3 parámetros separados

#Extraer algunas partes de una lista
mi_lista= [1,2,3,4,5,6]
a,*b, c, d = mi_lista
print(a,b,c,d)

#Unir lista
lista1= [1,2,3]
lista2 = [4,5,6]
lista3= [lista1,lista2]

print(f"Lista de listas: {lista3}")
lista3= [*lista1,*lista2] #Se desempaqueta lista1 y lista2
print(f"Unica lista: {lista3}")

#Unir diccionarios
dic1={"A":1,"B":2,"C":3}
dic2 = {"D":4,"E":5}
dic3 = {**dic1, **dic2}
print(f"Unir diccionarios: {dic3}")

#Construir una lista a partir de un str

listaStr = [*"HolaMundo"]
print(listaStr)
print(*listaStr)


