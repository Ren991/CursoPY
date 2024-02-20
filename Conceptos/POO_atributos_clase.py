class Persona:
    contador_personas = 0
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
    
# Mostrar los atributos de un objeto

persona1 = Persona("Juan","Perez")
print(persona1.__dict__) # Devuelve diccionario con atributos de instancia.

# Crear un atributo al vuelo

print(persona1.contador_personas) # => Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto , sino con la clase

persona1.contador_personas = 10

# Segundo objeto 
persona2 = Persona("Karla","Gomez")
print(persona2.__dict__)
print(persona2.contador_personas)

# Asociar atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)