

def numero(n):
    try:
        n = int(input(n))
        return n
    except ValueError:
        return None
    except TypeError:
        return None


entero = numero("Digite un numero: ")

try:
    if entero == None:
        print("Esto no es un numero entero")
    elif entero <0:
        print("No es un numero entero")
    else:
        print("Si es un numero entero")
except ValueError:
    print("Hubo un error")
except TypeError:
    print("Hubo otro error")