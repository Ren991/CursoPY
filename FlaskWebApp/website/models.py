# Acá se crean los modelos de la Base de datos
from . import db #=> Para importar SQLAlchemy
from flask_login import UserMixin #=> objeto predeterminado de usuario en flask.
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data= db.Column(db.String(10000))
    date= db.Column(db.DateTime(timezone=True), default= func.now())
    #ForeignKEY , es una columna que relaciona una tabla con otra
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # RELACION UN (usuario) a MUCHAS (nnotas)
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note") #Lista de notas del usuario
    
    