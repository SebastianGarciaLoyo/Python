while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Error. Numero entero no valido")

while True:
    try:
        num2 = int(input("Ingrese otro numero: "))
        break
    except ValueError:
        print("Error. Numero entero no valido.")

try:
    suma = num1 +num2
    print("La suma es: ", suma)
except Exception as e: #la e es un apodo para la excepcion general osea que esto es como una variable tipo alias :P
    print("Error al intentar sumar.\n"+ e)

