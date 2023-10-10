segundos = int(input("ingrese el valor en segundos: "))

hora = segundos//(60*60)

minutos = (segundos%(60*60))//60

segundos = (segundos%60)

print("{:,.0f}".format(hora))
print("{:,.0f}".format(minutos))
print("{:,.0f}".format(segundos))