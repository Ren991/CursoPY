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




