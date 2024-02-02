import psycopg2 

conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1', 
            port='5432',
            database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor: #=> un cursor es un objeto que nos permite ejecutar sentencia SQL en postgres
            sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)" #=> 3 parámetros
            valores= (("Pepe","Pipo","pipo@mail.com")
                      ,("Tito","Tuto","tito@mail.com"),
                      ("Coco","Coca","coco@mail.com")) #=> Tupla de tuplas
            cursor.executemany(sentencia,valores)
            #conexion.commit()#=> Guarda los cambios en base de dato
            registros_insertados = cursor.rowcount #=> rowcount devuelve cantidad de registros 
            print(f"Registros Insertados: {registros_insertados}")
                                   
            
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()