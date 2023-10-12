fd = open("Archivos/mbox-short.txt", "r")

cl = 0
cp = 0
for linea in fd:
    linea = linea.strip()
    #cp += len(linea.split())
    for lin in linea.split(" "):
        if lin.isalpha():
            cp += 1
    cl += 1
    
fd.close()
print("Cantidad de lineas: ", cl)
print("Cantidad de palabras: ", cp)