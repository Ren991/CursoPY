#Notas
# pip install flask
# pip install flask-login
# pip install flask-sqlalchemy (SQL)

from website import create_app

app = create_app()

if __name__ == "__main__": # Solo si corremos este archivo se ejecuta.
    app.run(debug=True)

