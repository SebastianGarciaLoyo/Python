def miFun(email):
    return email

fd = open("Archivos/mbox-short.txt", "r")

cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith("From:"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])

fd.close()
contarlineas = len(setEmail)
print("Cantidad de correos de origen distintos: ", cl)

for email in sorted(setEmail, reverse=False, key=miFun):
    print(email)