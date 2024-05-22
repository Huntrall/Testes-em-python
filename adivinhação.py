#A pessoa tem que adivinhar o número
import random

numero = random.randint(1, 101)

usuario = int(input('Adivinhe o número: '))
if usuario > numero:
    print('é um número menor')
elif usuario < numero:
    print('é um número maior')
while numero != usuario:
    usuario = int(input('Adivinhe o número: '))
    if usuario > numero:
        print('é um número menor')
    elif usuario < numero:
        print('é um número maior')