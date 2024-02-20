# Otras formas de crear objetos, dar posibilidad al usuario de crear objetos con diferentes valores

class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        
    @classmethod
    def crear_persona_vacia(cls):
        return cls(None,None) #=> Se llama al método init
    
    @classmethod
    def crear_persona_con_valores(cls,nombre,apellido):
        return cls(nombre,apellido)
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}. Apellido: {self.apellido}"
     
persona1= Persona("Pepe","Sanchez") # => Forma1
persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)

persona_con_valores = Persona.crear_persona_con_valores("Karla","Gomez")
print(persona_con_valores)