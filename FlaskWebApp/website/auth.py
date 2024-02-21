from flask import Blueprint, render_template # BluePrint significa que tiene muchas url definidas. 

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    #return render_template("login.html", text="Testing", user="Tim") # Así se pasan datos a través de las pantallas.
    return render_template("login.html", boolean=False)
@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")
