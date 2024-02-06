from cursorDelPool import CursorDelPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO: #=> DAO - DATA ACCES OBJECT = PATRON DE DISEÑO
    _SELECT = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s "
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug("Seleccionando usuarios")
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"usuario a insertar:{usuario}")
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount #=> ROWCOUNT devuelve cantidad de registros insertados

    
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario a actualizar {usuario}")
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario a eliminar: {usuario}")
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR , valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    
    #INSERTAR un  registro
    usuario1 = Usuario(username = "Ale", password="1234")
    usuarios = UsuarioDAO.insertar(usuario1)
    log.debug(f"Usuarios insertados: {usuarios}")
    #ACTUALIZAR un registro
    """ persona1 = Persona(1,"Juan carlos","Juarez", "cjjuarez@mail.com")
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"personas actualizadas: {personas_actualizadas}") """
    #Eliminar registro
    
    """ persona1= Persona(id_persona=2)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas: {personas_eliminadas}") """
    
    #Seleccionar objetos
    personas = UsuarioDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
    