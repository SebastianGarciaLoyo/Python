palabra = input("Escriba la palabra: ")

if palabra.endswith(palabra):                   
    print(f"La palabra {palabra} es palindrome")
    print(palabra[::-1])
else:
    print(f"la palabra {palabra}no es palindrome")

