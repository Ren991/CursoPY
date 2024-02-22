'''Todas las rutas que no sean auth
van acá
'''
from flask import Blueprint, render_template # BluePrint significa que tiene muchas url definidas. 
from flask_login import login_required, current_user


views = Blueprint("views", __name__)

@views.route("/")

@login_required
def home(): #Esta función se ejecuta siempre que vayamos a la ruta mencionada arriba
    return render_template("home.html", user=current_user)

