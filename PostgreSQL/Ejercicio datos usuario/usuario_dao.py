class UsuarioDAO: #=> DAO - DATA ACCES OBJECT = PATRON DE DISEÑO
    _SELECT = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERT = "INSERT INTO usuario(username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s "
    _ELIMINAR = "DETE FROM usuario WHERE id_usuario=%s"
    