def calculartarifabasica(estrato):
    if estrato == 1:
        return 10000
    elif estrato == 2:
        return 15000
    elif estrato == 3:
        return 20000
    elif estrato == 4:
        return 25000
    else:
        return 30000
    
def calcularvalorimpulso(impulso):
    return 100 * impulso



def leerestrato(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            if n <1 or n >5:
                print("Estrato invalido. ingrese un numero del 1 al 5")
                continue
            return n
        except ValueError:
            print("Error al ingresar su estrato.")




def leernombre(mensaje):
    while True:
        try:
            nombre = input(mensaje)
            nombre = nombre.strip()
            if len(nombre) == 0 or nombre.isalnum() == False:
                print("Nombre ")
                continue
            return nombre
        except Exception as e:
            print("Error al colocar el nombre", e)


def leerint(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            if n <1:
                print("Valor invalido. debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el numero.")

n = leerint("Ingrese la cantidad de usuarios: ")
valortotal = 0
for i in range(1, n+1):
    print("\nDatos del usuario #", i)
    nombre = leernombre("Nombre?: ")
    estrato = leerestrato("Estrato?: ")
    impulso = leerint("Impulso?: ")
    valortarifa = calculartarifabasica(estrato)
    valorimpulso = calcularvalorimpulso(impulso)

    print("=" *30)
    print("Nombre:",nombre)
    print("Tarifa:",valortarifa)
    print("Valor de impulsos:", valorimpulso)

    valortotal += valortarifa + valorimpulso

print("\n","*"*30)
print("El valor total a pagar es: ",valortotal)
