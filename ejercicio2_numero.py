
numeros_usuario = []
numero = ""
pregunta = ""

while pregunta != "No":
    numero = int(input("Dime un número: "))
    numeros_usuario.append(numero)
    pregunta = input("¿Quieres escribir un número? (Si / No) ")
num_list = 0
for num in numeros_usuario:
    num_list += 1

print("Hay {} números en la lista".format(num_list))