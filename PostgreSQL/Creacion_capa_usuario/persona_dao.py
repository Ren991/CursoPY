from conexion import Conexion
from persona import Persona
from cursor_del_pool import CursorDelPool

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
        
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        
         with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR , valores)
            log.debug(f"Persona insertada: {persona}")
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {persona}")
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, persona):
        
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Objeto eliminado: {persona}")
            return cursor.rowcount

if __name__ == "__main__":
    
    #INSERTAR un  registro
    persona1 = Persona(nombre = "Ale", apellido= "Martinez", email= "ale@mail.com")
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")
    #ACTUALIZAR un registro
    """ persona1 = Persona(1,"Juan carlos","Juarez", "cjjuarez@mail.com")
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"personas actualizadas: {personas_actualizadas}") """
    #Eliminar registro
    
    """ persona1= Persona(id_persona=2)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas: {personas_eliminadas}") """
    
    #Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
        