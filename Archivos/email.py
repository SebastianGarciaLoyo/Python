fd = open("Archivos/mbox-short.txt", "r")

email = set()
for linea in fd:
    if linea.startswith("To:"):
        email.add(linea.split()[1])

fd.close()
contarlineas = len(email)
print("Mensaje enviando:", )

for email in sorted(email, reverse=True):
    print(f"{email} Enviado [ok]")

hello = open("Archivos/mbox-short.txt", "r")






hello.close()
