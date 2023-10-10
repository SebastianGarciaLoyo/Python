nombre = input("Nombre del estudiante: ")
nota = int(input("Ingrese una nota: "))

if nota >= 0 and nota <= 59:
    notaCual= "D"
elif nota >= 60 and nota <= 79:
    notaCual= "C"
elif nota >= 80 and nota <= 89:
    notaCual= "B"
elif nota >= 90 and nota <= 100:
    notaCual= "A"
else:
    notaCual =""
    print("Error nota invalida")

print("\n","_"* 30)
print("Estudiante:", nombre)
print("Nota Cuantitatica:", nota)
print("Nota Cualitativa:", notaCual)