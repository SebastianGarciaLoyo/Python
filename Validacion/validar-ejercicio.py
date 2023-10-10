
hago = True

while hago:
    while True:
        try:
            nombre = input("Ingrese su nombre: ")
            codigo = int(input("Ingrese su codigo: "))
            progamaacademico = int(input("Ingrese su progama academio(1,2 o 3)"))
            indicadorbeca = int(input("Ingrese el nivel de su beca(1,2 o 3)"))
            if progamaacademico <1 or progamaacademico >3:
                print("Introduzca bien la categoria (1,2 o 3)") 
            elif   indicadorbeca <1 or indicadorbeca >3:
                print("Introduzca bien la beca (1,2 o 3)")
       
                continue
            break
        except Exception as e:
            print("Hubo un error, Vuelva a intentarlo")

            
    #Matematicas again...
    if progamaacademico == 1:
        valormatricula = 800_000
    elif progamaacademico == 2:
        valormatricula = 1_000_000
    elif progamaacademico == 3:
        valormatricula = 1_200_000

    

    if indicadorbeca == 1:
        valordescuento = 50
    elif indicadorbeca == 2:
        valordescuento = 40



    if progamaacademico == 1 and indicadorbeca == 1:
        valortotal = (valormatricula - valordescuento)
        print(f"El valor total es: ${valortotal:,.0f} ")
            
    elif progamaacademico == 2 and indicadorbeca == 2:
        valortotal = (valormatricula - valordescuento)
        print(f"El valor total es: ${valortotal:,.0f} ")  

    elif progamaacademico == 3 and indicadorbeca == 3:
        valortotal = (valormatricula - valordescuento)
        print(f"El valor total es: ${valortotal:,.0f} ")
    

    continuar = input("Desea continuar S O N: ")
    if continuar == "S" or continuar == "s":
        hago = True
    elif continuar == "N" or continuar == "n":
        hago = False

    print("\n", "="*30)
    print(f"Nombre: {nombre}")
    print(f"Codigo: {codigo}")
    print(f"Progama: {progamaacademico}")
    print(f"Beca: {indicadorbeca}")
    print(f"Valor: ${valortotal:,.0f}")
    print("\n", "="*30)
