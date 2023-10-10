# Función para validar si un número es entero
def es_entero(numero):
    return isinstance(numero, int)

# Función para generar números primos en un rango [n, m)
def numeros_primos_en_rango(n, m):
    primos = []
    for num in range(n, m):
        if num < 2:
            continue
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

# Función para la serie matemática
def serie_matematica(N):
    if N < 1:
        return 0
    resultado = 0
    for i in range(1, N + 1):
        resultado += i**2
    return resultado

# Programa principal
try:
    rango_inicial = int(input("Ingrese el rango inicial (n >= 2): "))
    rango_final = int(input("Ingrese el rango final: "))
    
    if rango_inicial < 2:
        print("El rango inicial debe ser mayor o igual a 2.")
    else:
        numeros_primos = numeros_primos_en_rango(rango_inicial, rango_final)
        cantidad_primos = len(numeros_primos)
        
        print(f"Los números primos entre [{rango_inicial} y {rango_final}) son: {numeros_primos}")
        print(f"La cantidad de números primos encontrados es: {cantidad_primos}")
        
except ValueError:
    print("Debe ingresar valores enteros válidos para los rangos.")
