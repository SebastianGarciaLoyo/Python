#Definir la funcion
def longString(str):
    try:
        long = 0
        while str[long] != None:
            long += 1
    except:
        pass
    return long
def prepararCafe(insumo1, insummo2):
    salida = ""
    if insumo1.lower() == "cafe" and insummo2 == "agua":
        salida = "tinto"
    else:
        salida = "Daño la cafetera"
    
    return salida

#Uso de la funcion
taza = prepararCafe("cafe","agua" )
print(taza)
print(longString(taza))
