# Hace que la carpeta sea un python package.

from flask import Flask

def create_app():
    app = Flask(__name__) # Representa el nombre del archivo
    app.config["SECRET_KEY"] = "clave_prueba_app" # Encripta y asegura la sesion 
    
    return app

