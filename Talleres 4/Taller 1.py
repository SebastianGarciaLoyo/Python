num = int(input("ESCRIBE UN NUMERO CUALQUIERA: "))

#crear una variable
suma_divisores = 0

#Iterar desde 1 hasta el número - 1
for i in range(1, num):

#Verificar si i es un divisor del número
    if num % i == 0:
        suma_divisores += i

#Verificar si la suma de los divisores es igual al número
if suma_divisores == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")








