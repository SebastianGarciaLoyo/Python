#Diseñar un progama en el que se pueda jugar tictactoe y tambien mostrar una tabla en el que salgan los mejores.
import json

def guardarlibro(lstjugador,ruta):

    try:
        fd = open(ruta,"w")
    except Exception as l:
        print("Error al abrir el archivo para guardar tu libro.\n", l)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstjugador,fd)
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

def existecodigo(nombre,lstjugador):
    
    for i, datos in enumerate(lstjugador):
    
        k = (list(datos.keys())[0])
        if k == nombre:
            return i
    return -1

def agregarjugador(lstjugador,ruta):
    print("\n\n1. Agregar Libro")

    nombre = int(input("Ingrese el CODIGO: "))
    while existecodigo(nombre,lstjugador) != -1:
        print("--> Ya existe un libro con este codigo")
        input("Presione cualquier tecla para continuar\n")
        nombre = (input("\nIngrese el Nombre again...: "))
    
    idjugador = (input("Nombre: "))
    

    dicnombre = {}
    dicnombre[nombre] = {"Nombre": idjugador,}
    lstjugador.append(dicnombre)

    if guardarlibro(lstjugador,ruta) == True:
        input("El Nombre ha sido registrado con exito.\nPresione cualquier tecla para continuar")
    else:
        input("Ocurrio algun error al guardar el nombre.")




def tabla(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("---"*len(fila))


def ganador(tablero,jugador):
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    
    for col in range(len(tablero[0])):
        if all(tablero[fila][col]== jugador for fila in range(len(tablero))):
            return True
    
    if all(tablero[i][i]== jugador for i in range(len(tablero))) or \
        all(tablero[i][len(tablero)-1-i] == jugador for i in range(len(tablero))):
        return True
    return False

def jugartictactoe(idjugador):
    tablero = [[" "for _ in range(3)]for _ in range(3)]
    jugador = "X"
    nombre = input("Ingrese su nombre: ")
    nombre2 = input("Ingrese su nombre tambien: ")
    while True:
        tabla(tablero)
        fila = int(input(f"{nombre} {jugador}, elige una fila (0,1,2): "))
        col = int(input(f"{nombre} {jugador}, elige una columna (0,1,2):"))

        if 0 <= fila < 3 and 0 <= col <3 and tablero[fila][col] == " ":
            tablero[fila][col] = jugador
            if ganador(tablero,jugador):
                tabla(tablero)
                print(f"Jugador {jugador} ha ganado!")
                break
            
            elif " " not in [casilla for fila in tablero for casilla in fila]:
                tabla(tablero)
                print("El juego termino en un empate :(")
            jugador = "X" if jugador == "O" else "O"
        else:
            print("Error,Movimiento no valido. Intente de nuevo.")


#Comienza la diversion :D
def menu():
    while True:
        try:
            print("*** Menu del juego ***")
            print("1.Agregar Jugador")
            print("2. Jugar!")
            print("3.Tabla de clasificacion")
            print("4.Salir")
            opcion = int(input("Opcion (1-4)? "))
            if opcion <1 or opcion >4:
                print("Opcion no valida. Escoja de 1 a 4.")
                input("Presione cualquier tecla para continuar...")
                continue
            return opcion
        except ValueError:
            print("Opcion no valida. Escoja de 1 a 4.")
            input("Presione cualquier tecla para continuar...")
def cargarinfo(lstjugador,ruta):
    try:
        fd = open(ruta,"r")
    except Exception as e:
        try:
            fd = open(ruta,"w")
        except Exception as d:
            print("Error al intentar abrir el archivo")
            input("Presione cualquier teclas para continuar")
        return None
    try:
        linea = fd.readline()
        if linea.strip() !="":
            fd.seek(0)
            lstjugador = json.load(fd)
        else:
            lstjugador = []
    except Exception as l:
        print("Error al cerrar el archivo.\n", l,"\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstjugador

#progama json
rutaFile = "juego/tabla.json"
lstjugador = []
lstjugador = cargarinfo(lstjugador,rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarjugador(lstjugador,rutaFile)
    elif op == 2:
        jugartictactoe(lstjugador)
    elif op == 3:
        pass
    else:
        print("Gracias por jugar :D ")
        break



