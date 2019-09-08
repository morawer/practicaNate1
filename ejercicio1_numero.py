numero = ""
numeros_usuario = []

while len(numeros_usuario) < 10:
    while not numero.isdigit():
        numero = input("Dime un número: ")
    numeros_usuario.append(int(numero))
    numero = ""
    print("Número añadido")

numero_pequeno = numeros_usuario [0]
for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print ("El número mas pequeño es: {}".format(numero_pequeno))

