from teclado import Teclado 
from raton import Raton
from monitor import Monitor
from computadora import Computadora
from orden import Orden

teclado1 = Teclado("HP", "USB")
raton1 = Raton("Acer", "USB")
monitor1 = Monitor("Asus",27)
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

teclado2 = Teclado("HP", "Bluetooth")
raton2 = Raton("Acer", "Bluetoot")
monitor2 = Monitor("Asus",45)
computadora2 = Computadora("HP", monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora1, computadora2]

orden = Orden(computadoras1)
print(orden)

