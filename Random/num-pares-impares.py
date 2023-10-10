num = int(input("Ingrese un numero: "))
pares = 0
impares = 0
while num != -1:
    if num % 2 == 0:
        print("El numero es par")
        pares += 1
    else:
        print("El numero es impar")
        impares += 1

    num = int(input("Ingrese un numero: "))
print("\n", "="* 30)
print("Cantidad de numero pares es: ",pares)
print("Cantidad de numero impares es: ",impares)
