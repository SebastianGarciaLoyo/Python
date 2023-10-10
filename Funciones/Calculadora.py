def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except:ZeroDivisionError
    resultado = None
    return resultado 




def calculadora():
    while True:
        try:
            print("*** Menu Calculadora ***")
            print("1.Sumar")
            print("2.Restar")
            print("3.Multiplicar")
            print("4.Dividir")
            print("5.Salir")
            opcion =int(input(">>> Opcion(1,5)?"))
            if opcion <1 or opcion >5:
                print("Opcion no valida. Escoja de 1 a 5.")
                continue
            return opcion
        except: ValueError
        print("Error opcion no valida.")
        print("Presione cualquier tecla para continuar")

        return opcion
    
def leerNum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error. Numero invalido")
            input("Presione cualquier tecla para continuar...")
# Progama principal
while True:
    opcion = calculadora()
    num1 = leerNum("Ingrese el primer numero: ")
    num2 = leerNum("Ingrese el segundo numero: ")
    if opcion == 1:
        print("\n\n1. SUMAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"EL resultado de la suma es:{suma(num1, num2):.3f}")
    elif opcion == 2:
        print("\n\n1. RESTAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"EL resultado de la suma es:{resta(num1, num2):.3f}")
    elif opcion == 3:
        print("\n\n1. MULTIPLICAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"EL resultado de la suma es:{multiplicacion(num1, num2):.3f}")
    elif opcion == 4:
        print("\n\n1. DIVISION")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"EL resultado de la suma es:{division(num1, num2):.3f}")
        res = division(num1, num2)
        if res != None:
            print(f"EL resultado de la suma es:{division(num1, num2):.3f}")
            
    elif opcion == 5:
        print("\n\nGracias por usar la calculadora")
        print("Adios")
        input()
        break
    input("Presione cualquier tecla para volver al MENU... ")

