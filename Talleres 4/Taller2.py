matricula = 10000  # Initial tuition amount
matricula2 = matricula * 2  # Double the initial tuition

años = 0  # Initialize the number of years

while matricula < matricula2:
    matricula *= 1.07  
    años += 1

print(f"Tomaria un total de {años} para que la matricula se multiplique .")
