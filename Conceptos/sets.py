#Un set es una colección de elementos únicos y es mutables
# Los elementos de un set deben ser inmutables
# Conjunto = {[1,2],[3,4]}

conjunto = {"Juan", True,19.0}
print(type(conjunto)) #=> Devuelve SET
# Set Vacío
conjunto = set()
#Agregar elementos
conjunto.add("Juan")
print(conjunto)
#Contiene valores únicos
conjunto.add("Juan")
print(conjunto)
# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto) #=> No se duplican los valores por ej 4 aparece una sola vez

# Podemos agregar mas elementos o incluso otro set

conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (copia poco profunda, solo copia referencias)

conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f"Igualdad en contenido? {conjunto == conjunto_copia}")
print(f"igualdad de referencia? {conjunto is conjunto_copia}")# Apuntan a la misma dirección de memoria ???


# OPERACIONES de conjuntos

#Personas con distintas características

pelo_negro = {"Juan","Carla","Pedro","Maria"}
pelo_rubio = {"Lorenzo","Laura","Marco"}
ojos_cafe = {"Karla", "Laura"}
menores_30 = {"Juan", "Karla", "Maria"}

#Todos con ojos cafe y pelo rubio( Union) ( no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativo)
print(f"Union pelo rubio y ojos cafe: {pelo_rubio.union(ojos_cafe)}")

# ( interesction) Solo las personas con ojos color cafe y pelo rubio
print(f"Interseccion café y pelo rubio {ojos_cafe.intersection(pelo_rubio)}")

# ( diference) => Diferencia de conjuntos . Pelo negro pero sin ojos color cafe
# Personas que se encuentran en el primer set pero no en el segundo
print(f"Diferencia entre pelo negro y ojos café: {pelo_negro.difference(ojos_cafe)}")

# Diferencia simétrica => Regresa todos los elementos excepto la intersección
print(f"Diferencia simétrica: {pelo_negro.symmetric_difference(ojos_cafe)}")




