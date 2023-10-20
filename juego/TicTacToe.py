import json
import time
#Imprime el tablero del juego
def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)
#funcion para revisar si alguien gano
def revisar_ganador(tablero, jugador):
    for fila in tablero:
        if all([casilla == jugador for casilla in fila]):
            return True
    for col in range(3):
        if all([tablero[fila][col] == jugador for fila in range(3)]):
            return True
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True
    return False
#SI llegado al caso el jugador que gane reemplaza al anterior que gano
def actualizar_tabla_de_puntuaciones(archivo, ganador, movimientos, tiempo_transcurrido):
    try:
        with open(archivo, 'r') as f:
            tabla_de_puntuaciones = json.load(f)
    except FileNotFoundError:
        tabla_de_puntuaciones = []

    tabla_de_puntuaciones.append({"jugador": ganador, "movimientos": movimientos, "tiempo": tiempo_transcurrido})

    with open(archivo, 'w') as f:
        json.dump(tabla_de_puntuaciones, f)
#Tabla de solo los jugadores que ganaron
def mostrar_tabla_de_puntuaciones(archivo):
    with open(archivo, 'r') as f:
        tabla_de_puntuaciones = json.load(f)
        print("Tabla de Puntuaciones:")
        print("Jugador\tMovimientos\tTiempo")
        for i, item in enumerate(tabla_de_puntuaciones):
            print(f"{i + 1}. {item['jugador']}\t{item['movimientos']}\t{item['tiempo']}")
#Progama del juego
def tres_en_raya():
    archivo = 'juego/puntuaciones.json'
    with open(archivo, 'w') as f:
        json.dump([], f)
    while True:
        tablero = [[' '] * 3 for _ in range(3)]
        print("¡Bienvenido a Tres en Raya!")
        jugador1 = input("Ingresa el nombre para el Jugador 1: ")
        jugador2 = input("Ingresa el nombre para el Jugador 2: ")
        marcador_j1 = input(f"{jugador1}, elige tu ficha 'X' o 'O': ").upper()
        marcador_j2 = 'X' if marcador_j1 == 'O' else 'O'
        print(f"{jugador1} jugará con {marcador_j1} y {jugador2} jugará con {marcador_j2}.")

        movimientos = 0
        tiempo_inicio = time.time()
        while True:
            imprimir_tablero(tablero)
            jugador = jugador1 if movimientos % 2 == 0 else jugador2
            marcador = marcador_j1 if movimientos % 2 == 0 else marcador_j2
            print(f"Turno de {jugador}.")
            while True:
                try:
                    x, y = map(int, input("Ingresa el número de fila y columna (índice de 0) separados por espacio: ").split())
                    if tablero[x][y] == ' ':
                        tablero[x][y] = marcador
                        break
                    else:
                        print("Esta posición ya está ocupada. Inténtalo de nuevo.")
                except ValueError:
                    print("Entrada no válida. Inténtalo de nuevo.")
                except IndexError:
                    print("Posición no válida. Inténtalo de nuevo.")

            if revisar_ganador(tablero, marcador):
                imprimir_tablero(tablero)
                print(f"¡Felicidades! ¡{jugador} ha ganado! ＼(^-^)／")
                tiempo_fin = time.time()
                tiempo_transcurrido = round(tiempo_fin - tiempo_inicio, 2)
                actualizar_tabla_de_puntuaciones(archivo, jugador, movimientos, tiempo_transcurrido)
                break
            movimientos += 1

            if movimientos == 9:
                imprimir_tablero(tablero)
                print("Es un empate suerte para la proxima ヽ(ヅ)ノ")
                break

        mostrar_tabla_de_puntuaciones(archivo)

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if jugar_nuevamente != 'sí':
            print("¡Gracias por jugar a Tres en Raya! ヘ(^_^ヘ)")
            break



def menu():
    while True:
        try:
            print("\n╔════════════════════════════════╗")
            print("║     ✨Menu TicTacToe✨         ║")
            print("╠════════════════════════════════╣")
            print("║ 1.Quieres jugar?               ║")
            print("║ 2.Tabla de clasificacion       ║")
            print("║ 3.Salir                        ║")
            print("╠════════════════════════════════╣")
            op = int(input("Eliga una opcion (1-3)"))
            if op < 1 or op >3:
                print("Opcion no valida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opcion no valida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")

## MENU
archivo = "juego/puntuaciones.json"
while True:
    op = menu()
    if op == 1:
        if __name__ == "__main__":
            tres_en_raya()
    elif op == 2:
        mostrar_tabla_de_puntuaciones(archivo)
    else:
        print("Gracias por jugar :D!")
        break