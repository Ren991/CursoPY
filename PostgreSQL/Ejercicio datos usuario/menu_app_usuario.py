from usuario_dao import UsuarioDAO
from logger_base import log
from usuario import Usuario

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
    elif opcion ==2:
        username_var = input("Escribe el nombre de usuario: ")
        password_var = input("Escriba la contraseña : ") 
        usuario = Usuario(username= username_var, password= password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f"Usuarios insertados: {usuarios_insertados}")
    
    elif opcion == 3:
        id_usuario_var = int(input("Escribe el id_usuario a modificar: "))
        username_var= input("Escribe el nuevo nombre de usuario : ")      
        password_var = input("Escribe la nueva contraseña: ")
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f"Usuarios actualizados: {usuarios_actualizados}")
        
    elif opcion == 4:
        id_usuario_var = int(input("Ingrese el id_usuario a eliminar : "))
        usuario = Usuario(id_usuario = id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f"Usuarios eliminados: {usuarios_eliminados}")
             
else:
    log.info("Salimos de la aplicacion")
    