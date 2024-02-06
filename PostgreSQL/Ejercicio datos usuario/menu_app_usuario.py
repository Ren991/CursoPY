from usuario_dao import UsuarioDAO
from logger_base import log

opcion = None

while opcion != 5:
    print("opciones:")
    print("1. Listar usuarios")
    print("2. Agregar usuario")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. salir")
    
    opcion= int(input("Escribe tu opcion (1-5):"))
    
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
            
else:
    log.info("Salimos de la aplicacion")
    