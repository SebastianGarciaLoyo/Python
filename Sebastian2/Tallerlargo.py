import math

# Función para calcular combinaciones
def calcular_combinatoria(n, k):
    if n < k:
        return "El valor de 'n' debe ser mayor o igual que 'k'"
    
    combinacion = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return combinacion

# Función para convertir texto a número
def quitar_texto(cadena):
    numeros = ''.join(filter(str.isdigit, cadena))
    return numeros

# Función para calcular el total de una factura con IVA
def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva):
    total = cantidad_sin_iva + (cantidad_sin_iva * (porcentaje_iva / 100))
    return total

# Menú principal
while True:
    print("\nMENU")
    print("1- Cálculo de la combinatoria")
    print("2- Convertir texto a número")
    print("3- Calcular el IVA de una factura")
    print("4- Salir")
    opcion = input("Escoja una opción (1-4): ")

    if opcion == '1':
        n = int(input("Ingrese el valor de 'n': "))
        k = int(input("Ingrese el valor de 'k': "))
        resultado = calcular_combinatoria(n, k)
        print(f"El valor de C({n}, {k}) es: {resultado}")
    elif opcion == '2':
        datos = input("Ingrese la cadena con textos y números: ")
        resultado = quitar_texto(datos)
        print(f"El resultado después de quitar los textos es: {resultado}")
    elif opcion == '3':
        cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))
        porcentaje_iva = float(input("Ingrese el porcentaje de IVA a aplicar: "))
        total = calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva)
        print(f"El total de la factura con IVA es: {total}")
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida (1-4).")
