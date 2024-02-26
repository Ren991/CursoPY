# Leer archivo json
# JSON = JavaScript Object Notation
import urllib.request
import json

peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

respuesta = urllib.request.urlopen(peticion)
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)

json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
print(json_respuesta)

# imprimir solo los nombre de las personas
# JSON se convierte a lista y diccionarios en python

for persona in json_respuesta['personas']:
    print(persona['nombre'], persona['edad'])
# Accedemos al total de personas de archivo
print(f'Total de personas: {json_respuesta["total"]}')
# Accedemos al mensaje del archivo
print(f'Mensaje: {json_respuesta["mensaje"]}')
