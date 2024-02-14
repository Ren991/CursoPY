# Leer contenido online
import urllib
from urllib.request import urlopen

palabras = []

peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
print(palabras)

#Contar ocurrencias cadena 
cadena ="Hola prueba python cadena"
print("N° Veces letra a:",cadena.count("a"))

#upper convierte a mayúscula un str
print(cadena.upper())

#lower convierte a minúscula un str
print(cadena.lower())

#método para determinar si una cadena se encuentra dentro de otra cadena 

print("Hola" in cadena) #=> Devuelve True si hola está en la variable cadena , de lo contrario devuelve False

# startwith - inicia con
print(cadena.startswith("Hola")) # retorna bool
#endswith - termina en 
print(cadena.endswith("pepe")) # retorna bool

#ALINEAR CADENA
titulo = "Prueba alinear cadena en python"

print(len(titulo))
#print(titulo.center(50,"*")) #=> rellena con * hacia ambos lados.
print(titulo.center(len(titulo)+10,"-"))

#ljust justifica a la izquierda
print(titulo.ljust(50,"*"))

#rjust justifica a la derecha
print(titulo.rjust(50,"*"))