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
            sentencia = "DELETE FROM persona WHERE id_persona=%s" #=> consulta Delete un parámetro.
            entrada= input("Proporciona el id_persona a eliminar: ")
            valores = (entrada,)
            cursor.execute(sentencia,valores)
            #conexion.commit()#=> Guarda los cambios en base de dato
            registros_eliminados = cursor.rowcount #=> rowcount devuelve cantidad de registros 
            print(f"Registros eliminados: {registros_eliminados}")
                                   
            
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()