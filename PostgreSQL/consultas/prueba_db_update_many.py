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
            sentencia = "UPDATE persona set nombre=%s, apellido=%s, email=%s WHERE id_persona=%s" #=> consulta update 4 parámetros
            valores = (("Juan","Perez","jperez@mail.com",1),
                       ("Ivonne","Gutierrez","igutierrez@mail.com",2),
                      )
            cursor.executemany(sentencia,valores)
            #conexion.commit()#=> Guarda los cambios en base de dato
            registros_actualizados = cursor.rowcount #=> rowcount devuelve cantidad de registros 
            print(f"Registros actualizados: {registros_actualizados}")
                                   
            
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()