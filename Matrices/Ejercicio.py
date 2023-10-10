filas = int(input("Cuantas filas tendra su matriz?: "))
columnas = int(input("Cuantas columnas tendra su matriz?: "))

matrix = []

for row_posicion in range(filas):
    row = []
    for element in range(columnas):
        row.append(int(input(f"Introduce un elemento a la fila {row_posicion}: ")))
    matrix.append(row)

for row in matrix:
    print(row)