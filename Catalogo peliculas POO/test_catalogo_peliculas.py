from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas


opcion = None

while opcion != 4:
    try:
        
        print("Opciones:")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Eliminar catálogo películas")
        print("4. Salir")
        
        opcion = int(input("Escriba tu opción (1-4): "))
        
        if opcion == 1:
            nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_peliculas(pelicula)
        
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()
        
            
            
    except Exception as e:
        print(f"Ocurrió un error {e}")
        opcion = None
else:
    print("Saliendo del programa...")
