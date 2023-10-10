
def descuento (valorarticulo):
    
    if valorarticulo > 150000:
        descuento = valorarticulo * 0.05
    else:
        descuento = 0
    return descuento
    
valor = int(input("Ingrese el valor del articulo: "))
descuento = descuento(valor)
print(f"El descuento es: ${descuento:,}")