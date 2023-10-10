
cheked = True
#Valor
valortecnico = 800000
valordesarrollo = 1000000
valoranimacion = 1200000
becaacademica = 50
becacultural = 40
valormatricula = 0
#Progamacion
while cheked:

 codigo = int(input("Ingrese su codigo: "))
nombre = (input("Ingrese su nombre: "))
Progamaacademico = int(input("Ingrese el numero del progama academico que pertenece: "))
indicadorbeca= int(input("Ingrese el numero de su indicador de beca: "))
 
if Progamaacademico == 1 and indicadorbeca == 1:
    valordescontado= (valortecnico * becaacademica)/ 100
    valormatricula -= valordescontado

elif Progamaacademico == 2 and indicadorbeca == 2:
    valordescontado= (valordesarrollo * becacultural)/100
    valormatricula -= valordescontado

elif Progamaacademico == 3:
    valormatricula -= 0

