kilos = float(input("Ingrese el numero de kilos que pesa: "))
estatura = float(input("Ingrese la altura que usted mide: "))

#CONVERSION
kilospeso = kilos * 0.45359237
estaruraaltura = estatura * 0.0254

#OBTENIDO del imc
imc = estaruraaltura / (kilospeso ** 2)

# parte logica

if imc < 18.5:  
    print("Estas en mala forma: {:,.1f}".format(imc))