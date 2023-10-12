archivo = open("Archivos/nombres.txt","r")

texto = archivo.read()
print(texto)

archivo.seek(0)
texto2 = archivo.readline()
print(texto2)

archivo.seek(2)
texto3 = archivo.readline()
print(texto3)
archivo.close()