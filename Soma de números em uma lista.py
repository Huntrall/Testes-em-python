#soma de números em uma lista
lista = []

jay = int(input('Escreva um número: '))
lista.append(jay)

while jay != 0:
    jay = int(input('Escreva um número: '))
    lista.append(jay)

resultado = sum(lista)

print(resultado)
