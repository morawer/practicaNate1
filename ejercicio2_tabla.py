input_numero = int(input("¿Que numero quieres introducir en la tabla? "))

for numero in range(1, 11):
    if numero % 2 == 0:
        print("{} x {} = {}".format(input_numero, numero, input_numero * numero))