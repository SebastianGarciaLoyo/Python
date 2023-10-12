fd = open("Archivos/nombres.txt", "r")

fd2 = open("Archivos/nombres_back.txt", "w")

for linea in fd:
    fd2.write(linea)



fd2.close()
fd.close()

print("Proceso terminado")