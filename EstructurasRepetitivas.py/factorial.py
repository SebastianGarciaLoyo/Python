#calcular el factorial de un numero
#factorial de 5 = 1 * 2 * 3 * 4 * 5

factorial = int(input("Numero? "))

fact = 1

for i in range(1, factorial+1):
    fact *= i

    print(f"EL factorial de {factorial} es {fact:,} ")
