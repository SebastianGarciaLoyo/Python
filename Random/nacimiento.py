fecha = input("fecha: ")
partes = fecha.split("/")
valido = True

if len(partes[0]) == 2 and \
    len(partes[1] == 2) and \
        len(partes[2] == 4):
    
    valido = True
    for p in partes:
            if not p.isdigit():
             valido = False
    
    if valido:
            print(f"dia:{partes[0]}, mes: {partes[1]}, años: {partes[2]}")
    else:
         print("Formato no valido")
          



