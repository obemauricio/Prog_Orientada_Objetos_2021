from library import Biblioteca
from libro_library import Libro

if __name__ == '__main__':
    
    ejecutar = True

    while(ejecutar):
        print('-------------BIBLIOTECA----------------')
        opcion = int(input('¿que vas a hacer?: \n1- Crear Biblioteca\n2- Agregar libro\n3- Ver catalogo\n4- Quitar libro\n5- Salir\n: '))

        if opcion == 1:
            nombre = input('Nombre de la biblioteca: ')
            biblioteca = Biblioteca(nombre)

            print(f'Se creo la biblioteca {biblioteca}'.format(biblioteca.consultar_nombre_biblioteca))
        
        elif opcion == 2:
            titulo = input('Titulo: ')
            autor = input('Autor: ')
            cantidad_de_paginas = input('Paginas: ')
            genero = input('Genero: ')
            sinopsis = input('Sinopsis: ')

            libro = Libro(titulo, autor, cantidad_de_paginas, genero. sinopsis)
            Biblioteca.agregar_libro(libro)
        
        elif opcion == 3:
            print('catalogo de libros: ')
            for i in Biblioteca.consultar_libros()
            print(i)
        
        elif opcion == 4:
            indice == input('Id del libro a eliminar: ')
            biblioteca.quitar_libro(indice)
        
        elif opcion == 5:
            ejecutar = False

        else:
            print('Opcion incorrecta')
