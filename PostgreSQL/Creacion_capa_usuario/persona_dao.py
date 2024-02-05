from persona import Persona
from conexion import Conexion
from logger_base import log

class PersonaDAO:
    '''
    DAO ( Data Acces Objetct) => Patron para trabajar con bases de datos.
    '''
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre,apellido, email) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s , apellido=%s, email=%s WHERE id_persona=%s "
    _ELIMINAR = "DELETE FROM persona where id_persona=%s "
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR , valores)
                log.debug(f"Persona insertada: {persona}")
                return cursor.rowcount
        

if __name__ == "__main__":
    
    #INSERTAR en registro
    persona1 = Persona(nombre = "Pepe", apellido= "Rodriguez", email= "peperod@mail.com")
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")
    #Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
        