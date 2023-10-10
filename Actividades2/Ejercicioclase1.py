#Diseñe y escriba un progama que solicite tres numeros enteros 
#( pueden ser positivos o negativos) y como salida los muestre en orden de mayor o menor

num1= int(input("1/3 ingrese un numero a continuacion: "))
num2= int(input("2/3 ingrese un numero a continuacion: "))
num3= int(input("3/3 ingrese un numero a continuacion: "))

if num1 > num2 or num1 > num3:
    numeromayor = num1
elif num2 < num1 or num2 > num3:
    numeromayor = num2
elif num3 > num2 or num3 > num1:
    numeromayor = num3

if num1 > num2 or num1 < num3:
 numeromenor = num1
elif num2 < num1 or num2 > num3:
    numeromenor = num2
elif num3 > num2 or num3 > num1:
    numeromenor = num3

if num1 > num2 or num1 > num3:
    numerointermedio = num1
elif num2 < num1 or num2 > num3:
    numerointermedio = num2
elif num3 > num2 or num3 > num1:
    numerointermedio = num3



print(numeromayor)
print(numeromenor)
print(numerointermedio)