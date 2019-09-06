
input_numero = int(input("¿Que numero quieres introducir en la tabla? "))
numeros = []

for numero in range(10, -1, -1):
    numeros.append(numero)

for num in numeros:
    print("{} x {} = {}".format(input_numero, num, input_numero * num))