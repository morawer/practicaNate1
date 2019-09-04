
frase_usuario = input("Introduce un texto: ")
mayusculas = 0
simbolos = [" ", ".", ","]
no_simbolo = 0
for letra in frase_usuario:
    if letra is simbolos:
        no_simbolo +=1
    if letra != letra.lower():
        mayusculas += 1
print("Hay {} mayusculas". format(mayusculas))
