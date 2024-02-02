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

            sentencia = "SELECT * FROM persona WHERE id_persona IN %s" #=> %s parámetro posicional, consulta sql
            #llaves_primarias = ((1,2,3),)
            #id_persona = input("Proporciona el valor id_persona: ")
            entrada = input("Propociona los id\´s a buscar (separado por comas): ")
            llaves_primarias = (tuple(entrada.split(",")),)
            
            cursor.execute(sentencia, llaves_primarias) #=> Se le pasa el parámetro de id_persona , tiene que ser tupla
            registros = cursor.fetchall() #=> fetchall() consulta todos los registros || fetchone() consulta un solo registros
            for registro in registros:
                print(registro)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()
