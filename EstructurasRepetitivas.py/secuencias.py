#Ejercicio 1
#Hacer un progama en python que genere el siguiente numero de la secuencia:
#1,1,2,-1,1,-2,?

n1 = 1
n2 = 1
sig = -1
print(n1, n2, end=", ")
for i in range(5):
    s = n1 + (sig**i) * n2
    n1 = n2
    n2 = s
    print(n1, n2, end=", ")