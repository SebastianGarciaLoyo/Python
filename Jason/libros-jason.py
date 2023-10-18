#Crear un progama que le permita al usuario agregar un libro como tambien ver el libro en una lista que este puesta de mayor a menor.


#Creando las funciones.

import json

def guardarlibro(lstlibros,ruta):

    try:
        fd = open(ruta,"w")
    except Exception as l:
        print("Error al abrir el archivo para guardar tu libro.\n", l)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstlibros,fd)
    except Exception as l:
        print("Error al guardar la informacion del libro.\n", l)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as l:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla pra continuar\n")
        return False
    
    return True

def existecodigo(codigo,lstcodigo):
    
    for i, datos in enumerate(lstcodigo):
    
        k = int(list(datos.keys())[0])
        if k == codigo:
            return i
    return -1

def agregarlibro(lstlibros,ruta):
    print("\n\n1. Agregar Libro")

    codigo = int(input("Ingrese el CODIGO: "))
    while existecodigo(codigo,lstlibros) != -1:
        print("--> Ya existe un libro con este codigo")
        input("Presione cualquier tecla para continuar\n")
        codigo = int(input("\nIngrese el CODIGO again...: "))
    
    id = int(input("Codigo: "))
    titulo = input("Titulo: ")
    autor = input("Autor del libro?: ")
    precio = int(input("Precio del libro?: "))

    diclibro = {}
    diclibro[codigo] = {"codigo": id, "titulo":titulo, "autor":autor, "precio":precio}
    lstlibros.append(diclibro)

    if guardarlibro(lstlibros,ruta) == True:
        input("El libro ha sido registrado con exito.\nPresione cualquier tecla para continuar")
    else:
        input("Ocurrio algun error al guardar el libro.")


def mayoromenor(diclibro):
    diclibro.items()
    print(diclibro)


def listamayoromenor(rutaFile):
    lista = sorted(rutaFile,key=mayoromenor)
    print(lista) 

def borrarlibro(lstlibros,rutaFile):
    print("\n\nBorrar Libro\n")
    codigo = int(input("Ingrese el codigo: "))
    if existecodigo(codigo, lstlibros) == -1:
        print("No existe un libro con este codigo")
        input("Presione cualquier tecla para continuar\n")

    for i in range(len(lstlibros)):
        datos = lstlibros[i]
        k = int(list(datos.keys())[0])
        if k == codigo:
            del lstlibros[i]
            break
    
def nombreslibro(lstlibros):
    while True:
        try:
            dato = int(input(lstlibros))
            break
        except ValueError:
            print(lstlibros, "debe ser algo valido.")
        return dato

def ordenamiento_nombre(diclibro,titulo):
    for j in range(diclibro): 
        if lstlibros[j][titulo]>lstlibros[j+1][titulo]:
            print(j)

def editarlibro(lstlibros):
    print("\n\nModificar libro\n")
    codigo = int(input("Ingrese el codigo del libro: "))
    if existecodigo(codigo,lstlibros) == -1:
        print("No existe un libro con este codigo.")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    buscar = guardarlibro(lstlibros,rutaFile)
    if buscar == -1 or buscar == "":
        print("El codigo del libro no existe")
        input()
        return
    print("\n")
    while True:
        editar = int(input("\n1.Titulo\n2.Autor\n3.Precio\n"))
        if editar <1 or editar >3:
            print("hubo un error, debido a que debes ingresar un numero valido entre 1 o 3.")
            input()
        elif editar == 1:
            print("Que titulo desea ponerle a su libro?: ")
        elif editar == 2:
            print("Quien es el autor entonces?: ")
        elif editar == 3:
            print("Que tanto cuesta tu libro ahora?: ") 
            continue
        break

def menu():
    while True:
        try:
            print("\n"* 30)
            print("||| REGISTRO LIBRO |||".center(40))
            print("MENU".center(40))
            print("1.Insertar")
            print("2.Consultar")
            print("3.Editar Libro")
            print("4.Borrar Libro")
            print("5.Ordenamiento libros")
            print("6.Salir")
            opcion = int(input("Opcion (1,6?: "))
            if opcion < 1 or opcion > 6:
                print("Opcion no valida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return opcion
        except ValueError:
            print("Opcion no valida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")
def cargarinfo(lstlibros,ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo \n", d)
            input("Presione cualquier tecla para continuar\n")
        return None
    try:
        linea = fd.readline()
        if linea.strip() !="":
            fd.seek(0)
            lstlibros = json.load(fd)
        else:
            lstlibros = []
    except Exception as l:
        print("error al cargar la informacion\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None


    
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as l:
        print("Error al cerrar el archivo.\n", l,"\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstlibros


# progama principal
rutaFile = "Jason/lista.json"
lstlibros = []
lstlibros = cargarinfo(lstlibros,rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarlibro(lstlibros,rutaFile)
    elif op == 2:
        listamayoromenor(lstlibros)
    elif op == 3:
        editarlibro(lstlibros)
    elif op == 4:
        borrarlibro(lstlibros,rutaFile)
    elif op == 5:
        ordenamiento_nombre(nombreslibro,rutaFile)
    else:
        print("\nGracias por usar el progama")
        break

