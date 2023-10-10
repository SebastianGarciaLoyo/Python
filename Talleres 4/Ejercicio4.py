nombre = (input("Diga su nombre: "))
estrato = int(input("Diga su estrato: "))
checked = True
valorestrato = 0

if estrato == 1:
    valorestrato = 10000

elif estrato == 2:
    valorestrato = 15000

elif estrato == 3:
    valorestrato = 30000

elif estrato == 4:
    valorestrato = 50000

elif estrato == 5:
    valorestrato = 65000

else:
    print("Debes elegir un un numero del 1 al 5. ")


#Defininendo
while checked:
    print("\n", "="*40)
    print(f"Nombre:{nombre}")
    print(f"Estrato:{estrato}")

    continuar = input("Desea continuar con su consulta? S/N?: ")

    if continuar == "s" or continuar == "S":
        checked = True
    elif continuar == "n" or continuar == "N":
        checked = False
    else:
        print("Debes poner S o N.")
        checked = False