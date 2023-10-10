while True:
    try:
        nombre = input("Ingrese su nombre de usuario: ")
        nombre = nombre.strip()
        
        if len(nombre) == 0  or not nombre.isalnum() == False:
            print("Nombre invalido. Vuelvba a digitarlo")
            continue
        break
    
    except Exception as e:
            print("Error al ingresar el nombre.\n", e)
#Validar el estrato
while True:
    try:
        estrato = int(input("Ingrese el estrato(1 al 5): "))
        if estrato <1 or estrato >5:
             print("El estrato no existe en el rango(1 al 5), intentalo de nuevo")
             continue
        break
    except ValueError:
         print("Error al ingresar el estratro.")

if estrato == 1:
    tarifaBasica = 10000
elif estrato == 2:
    tarifaBasica = 15000
elif estrato == 3:
     tarifaBasica = 30000
elif estrato == 4:
     tarifaBasica = 50000
else:
    tarifaBasica = 60000

print("\n", "="* 30)
print("Nombre:", nombre)
print("Tarifa Basica:", tarifaBasica)

