nota = float(input("dijite una nota de 0.0 a 5:"))
curva = (nota * 0.8)+ 1

print("la curva del 8 de la nota"+ str(nota)+ "es:{:,.1f}".format(curva))