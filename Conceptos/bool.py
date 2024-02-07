# bool contiene los valores de True y False
# Tipos numéricos, False para 0, True demás valores
valor  = 0
resultado = bool(valor)

#print(f"Valor {valor}, resultado: {resultado}")

#Tipo str, False o True

valor  = ""
resultado = bool(valor)

#print(f"Valor {valor}, resultado: {resultado}")

# Tipo colecciones, False para colecciones vacías, True para las demas colecciones

valor  = [] # => también podría ser una tupla () - (1,2,3,4) o diccionario {nombre:"pepe",apellido:"pepito"} - {}
resultado = bool(valor)

print(f"Valor {valor}, resultado: {resultado}")


