#Un decorador es una funcion que recibe una funcion y regresa en otras
# Lo usamos para extender funcionalidad
# 1. Funcion decorador(a)
# 2. Funcion a decorar(b)
# 3. Funcion decorada(c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        print("Antes de ejecutar la funcion")
        funcion_a_decorar_b()
        print("Despues de ejecutar la funcion")
    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print("Hola desde funcion mostrar_mensaje")
    
mostrar_mensaje()

@funcion_decorador_a
def imprimir():
    print("Hola desde funcion imprimir")

imprimir()
