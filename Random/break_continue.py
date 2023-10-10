#Break
#Calcular si un numero es primo
#num primo: divisible por si mismo y por 1

#num = int(input("Ingrese un numero? "))

#if num < 2:
 #   print("No es primo")
#elif num == 2:
  #  print("Es primo")
#else:
  #  esprimo = True #variables tipo banderas
   # for i in range(2, num):
       # if num % i == 0:
       #  esprimo = False
       # break
    #
   # if esprimo:
      # print("Es primo")
   # else:
      # print("No es primo. Lo divide",i)


#CONTINUE

#Imprima los numeros del 1 al 100 excepto los multiplos del 7

for i in range(1,100):
    if i % 7 == 0:
       continue
    print(i, end=", ")