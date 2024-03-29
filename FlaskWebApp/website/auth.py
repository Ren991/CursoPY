from flask import Blueprint, render_template,request,flash,redirect,url_for # BluePrint significa que tiene muchas url definidas. 
from .models import User
from . import db # significa de __init__.py importar db
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import login_user, login_required, logout_user, current_user





auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    #return render_template("login.html", text="Testing", user="Tim") # Así se pasan datos a través de las pantallas.
    data = request.form
    print(data)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email = email).first() # Filtrar usuario
        if user:
            if check_password_hash(user.password, password):
                flash("Inicio sesión exitoso", category="success")
                login_user(user, remember=True) # recuerda el usuario que ingresó.
                return redirect(url_for('views.home'))
            else:
                flash("Contraseña incorrecta, intentelo de nuevo", category="error")
        else:
            flash("El email que ingresó no existe", category="error") 

    return render_template("login.html", user=current_user)
@auth.route("/logout")

@login_required #Decorador , solo funciona si el usuario se logueó previamente.
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        user = User.query.filter_by(email = email).first() # Filtrar usuario
        if user:
            flash("El mail ya existe", category="error")
            return redirect(url_for("auth.sign_up"))
        if len(email) < 4:
            flash("Email debe tener mas de 4 caracteres", category="error")
            pass
        elif len(firstName) < 2:
            flash("El campo Nombre debe tener mas de 1 caracter", category="error")

            pass
        elif password1 != password2:
            flash("Las contraseñas no coinciden", category="error")

            pass
        elif len(password1) < 7:
            flash("La contraseña debe tener como mínimo 7 caracteres", category="error")

            pass
        else:
            new_user = User(email=email, first_name= firstName, password=generate_password_hash(password1, method="pbkdf2:sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            # add user to database
            flash("Cuenta creada!!", category="success")
            return redirect(url_for("views.home"))
            
            
        
    return render_template("sign_up.html", user=current_user)
