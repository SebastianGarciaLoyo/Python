sueldoneto = 0

numerodehoras = int(input("digite el numero de horas trabajadas"))

valorhora = 20000
sueldobruto = valorhora * numerodehoras

eps = 0.04
pension = 0.04

apartado1 = sueldobruto * eps
apartado2 = sueldobruto * pension

sueldoneto = sueldobruto - apartado1 - apartado2
print("el sueldobruto es ${:,.1f}".format(sueldobruto))
print("el descuento por pension es ${:,.1f}".format(apartado1))
print("el descuento por pension es ${:,.1f}".format(apartado2))
print("su sueldo neto es ${:,.1f}".format(sueldoneto))