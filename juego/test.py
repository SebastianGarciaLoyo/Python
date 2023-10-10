import random

# Función para jugar una partida
def jugar_partida():
    numero_a_adivinar = random.randint(1, 1000)
    intentos = 0
    nombre = input("Por favor, introduce tu nombre: ")

    while intentos < 10:
        intento = int(input("Intento {}/10. Adivina el número (entre 1 y 1000): ".format(intentos + 1)))
        intentos += 1

        if intento < numero_a_adivinar:
            print("El número a adivinar es mayor.")
        elif intento > numero_a_adivinar:
            print("El número a adivinar es menor.")
        else:
            print("¡Felicitaciones, {}! Has adivinado el número en {} intentos.".format(nombre, intentos))
            return intentos

    print("Lo siento, has agotado tus 10 intentos. El número era {}.".format(numero_a_adivinar))
    return 10

# Función para mostrar la tabla de posiciones
def mostrar_tabla_posiciones(mejores_intentos):
    print("\nTabla de Posiciones (Los 10 Mejores):")
    for i, intentos in enumerate(mejores_intentos, start=1):
        print("{}. Intentos: {}".format(i, intentos))

# Función principal
def main():
    mejores_intentos = []

    while True:
        intentos = jugar_partida()
        mejores_intentos.append(intentos)
        mejores_intentos.sort()

        if len(mejores_intentos) > 10:
            mejores_intentos.pop()

        mostrar_tabla_posiciones(mejores_intentos)

        continuar = input("¿Deseas jugar de nuevo? (SI/NO): ").upper()
        if continuar != "SI":
            break

    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()
