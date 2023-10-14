fd = open("Archivos/mbox.txt", "r")

email = set()
for linea in fd:
    if linea.startswith("X-DSPAM-Confidence:"):
        email.add(linea.split()[1])

fd.close()
contarlineas = len(email)
print("Mensaje enviando:", )

for email in sorted(email, reverse=True):
    print(f"{email} Enviado [ok]")