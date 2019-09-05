
frase_usuario = input("Escribe una frase: ").lower()
vocales = ["a", "e", "i", "o", "u"]
lista_vocales = []

for letra in frase_usuario:
    if letra in vocales:
        lista_vocales.append(letra)

print("vocales = {}".format(lista_vocales))
