import json

fd = open("Jason/lista.json","r")

lista = []

lst = json.load(fd)


for e in lst:
    print(f"Nombre: {e['Nombre']}")
    print(f"Edad: {e['edad']}")
    print("-"*30)


fd.close()