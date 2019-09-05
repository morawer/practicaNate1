
frase_usuario = input("Introduce un texto: ")
mayusculas = 0

for letra in frase_usuario:
    if letra.isupper():
        mayusculas += 1
print("Hay {} mayusculas". format(mayusculas))
