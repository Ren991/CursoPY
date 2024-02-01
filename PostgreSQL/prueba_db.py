import psycopg2 

conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1', 
            port='5432',
            database='test_db')


cursor = conexion.cursor() #=> un cursor es un objeto que nos permite ejecutar sentencia SQL en postgres

sentencia = "SELECT * FROM persona" #=> consulta sql

cursor.execute(sentencia)
registros = cursor.fetchall()

print(registros)

cursor.close()
conexion.close()
