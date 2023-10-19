import json
import time

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

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

def actualizar_tabla_de_puntuaciones(archivo, ganador, movimientos, tiempo_transcurrido):
    with open(archivo, 'r') as f:
        tabla_de_puntuaciones = json.load(f)
        tabla_de_puntuaciones.append({"jugador": ganador, "movimientos": movimientos, "tiempo": tiempo_transcurrido})
        tabla_de_puntuaciones.sort(key=lambda x: (x["movimientos"], x["tiempo"]))
    with open(archivo, 'w') as f:
        json.dump(tabla_de_puntuaciones, f)

def mostrar_tabla_de_puntuaciones(archivo):
    with open(archivo, 'r') as f:
        tabla_de_puntuaciones = json.load(f)
        print("Tabla de Puntuaciones:")
        print("Jugador\tMovimientos\tTiempo")
        for i, item in enumerate(tabla_de_puntuaciones):
            print(f"{i + 1}. {item['jugador']}\t{item['movimientos']}\t{item['tiempo']}")

def tres_en_raya():
    archivo = 'puntuaciones.json'
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
                print(f"¡Felicidades! ¡{jugador} ha ganado!")
                tiempo_fin = time.time()
                tiempo_transcurrido = round(tiempo_fin - tiempo_inicio, 2)
                actualizar_tabla_de_puntuaciones(archivo, jugador, movimientos, tiempo_transcurrido)
                break
            movimientos += 1

            if movimientos == 9:
                imprimir_tablero(tablero)
                print("¡Es un empate!")
                break

        mostrar_tabla_de_puntuaciones(archivo)

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if jugar_nuevamente != 'sí':
            print("¡Gracias por jugar a Tres en Raya!")
            break

if __name__ == "__main__":
    tres_en_raya()

    
