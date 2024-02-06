from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        log.debug("Inicio del método with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug("Se ejecutó método __exit__")
        if valor_excepcion: 
            self._conexion.rollback()
            log.error(f"Ocurrió una excepcion, se hace rollback: { valor_excepcion} {tipo_excepcion} {detalle_excepcion}")
        else:
            self._conexion.commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
        
    