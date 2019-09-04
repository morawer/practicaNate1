
frase_usuario = input("Introduce un texto: ")

simbolos = [" ", ".", ","]

espacio = 0
punto = 0
coma = 0

for caracter in frase_usuario:
    if caracter is " ":
        espacio += 1
    elif caracter is ".":
        punto += 1
    elif caracter is ",":
        coma += 1

print("El texto contiene {} espacios, {} puntos y {} comas.".format(espacio, punto, coma))
