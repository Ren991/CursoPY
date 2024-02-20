# Ejemplos atributos públicos, protegidos, privados

class MiClase:
    def __init__(self, publico, protegido,privado) -> None:
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado
        
 
objeto = MiClase("Valor público", "Valor protegido", "valor privado")
# acceso al atributo público
print(objeto.publico)   
# Modificar el valor público

objeto.publico ="Nuevo valor público"
print(objeto.publico)

# Acceso al valor protegido
# solo dentro de la misma clase o clasees hijas
print(objeto._protegido) 

# Acceder al valor privado
#print(objeto.__privado) => Devuelve error
#Pero , convierte: objeto._clase__atributo_privado
print(objeto._MiClase__privado)