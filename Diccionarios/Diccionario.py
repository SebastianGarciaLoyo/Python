#empleado = {}
empleado = {"Nombre":"Segalo","Cargo":"Progamador","Salario":"40000"}
print(empleado["Cargo"])
print(empleado["Salario"])
print(empleado["Nombre"])
#print(empleado["apellido"])
print(empleado.get("apellido","llave no existe"))

#agregar una llave
empleado["sexo"] = "M"
print(empleado)

#Modificar un valor
empleado["salario"] = "5000000"
print(empleado)

#Borrar una llave y su valor
del empleado["sexo"]
print(empleado)

#Borrar todo el diccionario
#empleado = {}
#empleado.clear()
#del empleado


oficina = empleado.copy()
print(oficina)
oficina["progamador"] = 50000
print(oficina)
print(empleado)

#Items
print(empleado.items())

#Keys
print(empleado.keys())

#values
print(empleado.values())

#pop
print(empleado.pop("Salario"))
print(empleado)

#popitem
print(empleado.popitem())
print(empleado)

#setdefault
print(empleado.setdefault("Nombre","Segalo"))
print(empleado)
print(empleado.setdefault("Ciudad","Bucaramanga"))
print(empleado)