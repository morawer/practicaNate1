
frase_usuario = input("Introduce un texto: ").upper()
vocales = ["A", "E", "I", "O", "U"]
no_contar = [",", ".", " ", "¿", "?", "¡", "!"]

n_vocales = 0
n_consonantes = 0

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    elif letra not in no_contar:
        n_consonantes += 1

print("El texto tiene {} vocales y {} consonantes".format(n_vocales, n_consonantes))