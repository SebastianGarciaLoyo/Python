vidas = 10
numeraso = 150
from random import*
filas = 1
columnas = 1
randomizador = [[randint(1, 1000)for i in range(filas)]for j in range(columnas)]

    
for f in randomizador:

    usuario=[]    
    nombre = input(("Ingrese su nombre: "))
    usuario.append(nombre)
    print(usuario)

numero = int(input("Ingrese un numero entre el 1 al 1000: "))


while True:
    
        
    if numero == randomizador:
        print("Eso es correcto")
        if numero < 1 or numero > 1000:
            print("Error numero invalido")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(9/10)")
    
    intento2 = int(input("Ingrese otro numero:"))
    if intento2 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(8/10)")
    
    intento3 = int(input("Ingrese otro numero:"))
    if intento3 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(7/10)")
    
    intento4 = int(input("Ingrese otro numero:"))
    if intento4 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(6/10)")
    
    intento5 = int(input("Ingrese otro numero:"))
    if intento5 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(5/10)")
    
    intento6 = int(input("Ingrese otro numero:"))
    if intento6 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(4/10)")
    
    intento7 = int(input("Ingrese otro numero:"))
    if intento7 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(3/10)")
    
    intento8 = int(input("Ingrese otro numero:"))
    if intento8 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(2/10)")
    
    intento9 = int(input("Ingrese otro numero:"))
    if intento9 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(1/10)")
    
    intento10 = int(input("Ingrese otro numero:"))
    if intento10 == randomizador:
        print("Eso es correcto")
    elif numero != randomizador:
        vidas -= 1
        print("Incorrecto perdiste una vida(0/10)")
    if vidas == 0:
        print("GAME OVER >:D!") 
    
    if numeraso == randomizador:
        print("Felicidadades encontraste el numero :D!!!")   
        
    
    continuar = input("Desea continuar? Si o No?: ")
    if continuar == "Si": 
        print("Volvamos otra vez")
    else:
        print("Gracias por jugar")
        break