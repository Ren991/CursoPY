print(dir(__builtins__))

numeros = [1,2,3]
letras = ["a","b","c"]
mezcla = zip(numeros,letras)
print(mezcla)#=> Objeto de tipo zip

print(list(mezcla))#=> Lista que en cada indice tiene una tupla con un numero y una letra.
print(tuple(zip(numeros,letras)))#=> Tupla de tuplas

