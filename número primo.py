#contando número primo

numero = int(input('Insira um número inteiro: '))
tot = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        tot += 1

if tot == 2:
    print('seu número é primo')
else:
    print('5seu número não é primo')