import json


class Libro:
    def __init__(self, codigo, titulo, autor, precio):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def get_codigo(self):
        return self.codigo

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_precio(self):
        return self.precio

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'titulo': self.titulo,
            'autor': self.autor,
            'precio': self.precio
        }


def ordenar_por_codigo(libro):
    return libro.get_codigo()


def ordenar_por_titulo(libro):
    return libro.get_titulo()


def ordenar_por_autor(libro):
    return libro.get_autor()


def ordenar_por_precio(libro):
    return int(libro.get_precio())


libreria = []


def cargar_libreria():
    try:
        with open('libreria.json', 'r') as file:
            libros = json.load(file)
            for libro in libros:
                libreria.append(Libro(libro['codigo'], libro['titulo'], libro['autor'], libro['precio']))
    except FileNotFoundError:
        # Si no se encuentra el archivo, se crea uno vacío
        guardar_libreria()


def guardar_libreria():
    with open('libreria.json', 'w') as file:
        libros = [libro.to_dict() for libro in libreria]
        json.dump(libros, file, indent=4)


def insertar_libro():
    codigo = input("Ingrese el código del libro: ")
    for libro in libreria:
        if libro.get_codigo() == codigo:
            print("El código del libro ya existe. Intente de nuevo.")
            return
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    precio = input("Ingrese el precio del libro: ")
    libro = Libro(codigo, titulo, autor, precio)
    libreria.append(libro)
    libreria.sort(key=ordenar_por_codigo)
    guardar_libreria()
    print("Libro insertado con éxito.")


def buscar_libro():
    codigo = input("Ingrese el código del libro que desea buscar: ")
    for libro in libreria:
        if libro.get_codigo() == codigo:
            print(f"Código: {libro.get_codigo()}, Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Precio: {libro.get_precio()}")
            return
    print("Libro no encontrado.")


def editar_libro():
    codigo = input("Ingrese el código del libro que desea editar: ")
    for libro in libreria:
        if libro.get_codigo() == codigo:
            libro.titulo = input(f"Ingrese el nuevo título para el libro (anterior: {libro.get_titulo()}): ")
            libro.autor = input(f"Ingrese el nuevo autor para el libro (anterior: {libro.get_autor()}): ")
            libro.precio = input(f"Ingrese el nuevo precio para el libro (anterior: {libro.get_precio()}): ")
            guardar_libreria()
            print("Libro editado con éxito.")
            return
    print("Libro no encontrado.")


def borrar_libro():
    codigo = input("Ingrese el código del libro que desea borrar: ")
    for libro in libreria:
        if libro.get_codigo() == codigo:
            libreria.remove(libro)
            guardar_libreria()
            print("Libro eliminado con éxito.")
            return
    print("Libro no encontrado.")


def listar_por_nombre():
    libreria.sort(key=ordenar_por_titulo)
    mostrar_libros_paginados()


def listar_por_autor():
    libreria.sort(key=ordenar_por_autor)
    mostrar_libros_paginados()


def listar_por_precio():
    libreria.sort(reverse=True,key=ordenar_por_precio)
    mostrar_libros_paginados()


def mostrar_libros_paginados():
    for i in range(0, len(libreria), 3):
        for libro in libreria[i:i + 3]:
            print(f"Código: {libro.get_codigo()}, Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Precio: {libro.get_precio()}")
        input("Presione enter para ver más libros")


def mostrar_menu():
    cargar_libreria()  # Cargar la librería al inicio del programa
    while True:
        print("\n1. Insertar libro")
        print("2. Consultar libro por código")
        print("3. Editar libro")
        print("4. Borrar libro")
        print("5. Listar libros por nombre")
        print("6. Listar libros por autor")
        print("7. Listar libros por precio")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            insertar_libro()
        elif opcion == '2':
            buscar_libro()
        elif opcion == '3':
            editar_libro()
        elif opcion == '4':
            borrar_libro()
        elif opcion == '5':
            listar_por_nombre()
        elif opcion == '6':
            listar_por_autor()
        elif opcion == '7':
            listar_por_precio()
        elif opcion == '8':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    guardar_libreria()  # Guardar la librería al salir del programa


mostrar_menu()


