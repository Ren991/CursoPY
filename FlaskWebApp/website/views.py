'''Todas las rutas que no sean auth
van acá
'''
from flask import Blueprint # BluePrint significa que tiene muchas url definidas. 

views = Blueprint("views", __name__)

@views.route("/")
def home(): #Esta función se ejecuta siempre que vayamos a la ruta mencionada arriba
    return "<h1>Test</h1>"

