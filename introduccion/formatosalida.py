# Ejemplos de formatear la salida

#Con Format
sueldo = 5600000
print("Sueldo: ${:,}".format(sueldo))

interes = 2568.46567989468578875
print("interes: ${:,.3f}".format(interes))

#f-string
print(f"sueldo: ${sueldo:,}")
print(f"Valor del interes:{interes:,.3f}")