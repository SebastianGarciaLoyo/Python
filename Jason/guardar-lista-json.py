import json

fd = open("Jason/lista.json","r")

lista = ["hola"]

json.dump(lista,fd)


fd.close()
