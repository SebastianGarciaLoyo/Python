n = int(input("Cantidad de docentes?: "))

diccategoria ={1:25000, 2:30000, 3:40000, 4:45000, 5:60000}

dicdocentes ={}
totalHonorarios = 0

for i in range(1, n+1):
    print("\nDatos del Docente #", i)
    datdocente = {}
    cedula = input("Cedula: ")
    datdocente["Nombre"] = input("Nombre: ")
    datdocente["categoria"] = int(input("categoria(1 al 5):  "))
    datdocente["horas_lab"] = int(input("Horaslaborales: "))
    datdocente["honorarios"] = diccategoria.get(datdocente["categoria"], 0) * datdocente["horas_lab"] 

    totalHonorarios += datdocente["honorarios"]

    dicdocentes[cedula] = datdocente

print("\n\n", "=" *30)
print("INFORME")
print("=" *30)
print("NOMBRE\t\tHONORARIOS")
print("-" *30)

for k, v in dicdocentes.items():
    print(f'{v["Nombre"]}\t\t${totalHonorarios:,}') 

print("\n\n", "=" *30)
print(f"Totalhonorarios: ${totalHonorarios:,}")