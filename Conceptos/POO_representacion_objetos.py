# 3 formas para representar objetos en py (str, repr, format)

class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        
    # repr , más enfocado a los programadores
    
    def __repr__(self) -> str:
        return f"Persona(nombre:{self.nombre}, apellido:{self.apellido})"
    
persona1 = Persona("Juan","Perez")
print(persona1)


