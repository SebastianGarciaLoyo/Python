usuarios = int(input("Cuantos Usuarios? "))

for i in range(1, usuarios+1):
    print(f"\nDatos del usuario #{i}")
    codigousuario = input("Codigo? ")
    nombre = input("Nombre? ")
    estado = input("Estado [v:vigente o s:suspendido]? ")
    estrato = int(input("Estrato [1 al 6]? "))
    consumomes = float(input("Consumo agua al mes [cm3]? "))
    #Calcular la tarifa basica
    if estado == "V" or estado == "v":
        if estrato == 1:
            tbas = 10000
        elif estrato == 2:
            tbas = 20000
        elif estrato == 3:
            tbas = 30000
        elif estrato == 4:
            tbas = 45000
        elif estrato == 5:
            tbas = 60000
        elif estrato == 6:
            tbas = 70000
        else:
            tbas = 0
        #Calcular el consumo
        valorconsumo = consumomes * 200

        #Calcular el valor a pagar
        valorPagar = tbas + valorconsumo

        #imprimir el informe del usuario
        print(f"\n","="* 40)
        print(f"\t Nombre:", nombre)
        print(f"\tValor de la tarifa: ${tbas:,}")
        print(f"\tValor consumo: ${valorconsumo:,.0f}")
        print(f"\tValor de la factura de agua: ${valorPagar:,.0f}")
                            


