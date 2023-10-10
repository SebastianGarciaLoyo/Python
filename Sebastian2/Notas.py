
def resultado(n1,n2,n3,n4,n5):
    
    promedio = (n1+n2+n3+n4+n5) / 5
    if promedio >3.5:
        return True 
    else:
        return False

nota1 = float(input("Ingrese la nota1: "))
nota2 = float(input("Ingrese la nota2: "))
nota3 = float(input("Ingrese la nota3: "))
nota4 = float(input("Ingrese la nota4: "))
nota5 = float(input("Ingrese la nota5: "))

if resultado(nota1,nota2,nota3,nota4,nota5):
    print("Pasaste el año felicidades!")
else:
    print("Perdiste el año mala suerte...")
    
    