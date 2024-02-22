'''Todas las rutas que no sean auth
van acá
'''
from flask import Blueprint, render_template, request,flash,jsonify # BluePrint significa que tiene muchas url definidas. 
from flask_login import login_required, current_user
from .models import Note
from . import db 
import json





views = Blueprint("views", __name__)

@views.route("/", methods=["GET","POST"])


@login_required
def home(): #Esta función se ejecuta siempre que vayamos a la ruta mencionada arriba
    if request.method =="POST":
        note = request.form.get("note")
        if len(note) < 1:
            flash("La nota es demasiado corta!", category="error") 
        else:
            new_note = Note(data=note,user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Nota agregada!",category = "succes")
            
        
    return render_template("home.html", user=current_user)

@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"] 
    note = Note.query.get(noteId)
    print("Nota eliminada")
    if note:
        print("Hay notas")
        if note.user_id == current_user.id:
            print("Entra en la condicion")
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
    