from teclado import Teclado
from monitor import Monitor
from raton import Raton

class Computadora:
    contador_computadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton) -> None:
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado 
        self._raton = raton
    
    def __str__(self) -> str:
        return f'''
            {self._nombre}: {self._id_computadora}
            Monitor: {self._monitor}
            Teclado: {self._teclado}
            Ratón: {self._raton}
        '''

if __name__ == "__main__":
    
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("Acer", "USB")
    monitor1 = Monitor("Asus",27)
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)
    print(computadora1)
