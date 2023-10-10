while True:
    try:
        cat = int(input("Ingrese una categoria(1,2 o 3): "))
        if cat < 1 or cat > 3:
            print("No es una categoria invalida")
            continue
        break
    except ValueError:
        print("Error. Categoria invalida")