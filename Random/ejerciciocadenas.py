num = input("Ingrese el numero: ")

if num.startswith("+") and num.count("-") == 2:
    partes = num.split("-")
    print("EL telefono es: ", partes[1])
else:
    print("Error. El numero no cumple con el formato")