# Hace que la carpeta sea un python package.

from flask import Flask

def create_app():
    app = Flask(__name__) # Representa el nombre del archivo
    app.config["SECRET_KEY"] = "clave_prueba_app" # Encripta y asegura la sesion 
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    
    return app

