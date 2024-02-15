#Las listas son mutables

nombres1 = ["Juan","Karla","Pedro"]
nombres2 = "Laura María Gonzalo Ernesto".split()

#Sumar listas usando operador +

print(f"Sumar listas {nombres1+nombres2}")
#Extender una lista con otra lista

nombres1.extend(nombres2) # Se le agrega a la lista "nombres1" los elementos de la lista "nombres2"
print(f"Exntender la lista1 {nombres1}")


