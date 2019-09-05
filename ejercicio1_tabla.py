
input_numero = int(input("¿Que numero quieres introducir en la tabla? "))

for numero in range(5, 16):
    print("{} x {} = {}".format(input_numero, numero, input_numero * numero))