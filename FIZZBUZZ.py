#Contagem de 1 a 100 e fale fizz para multiplos de 3 e buzz para 5 e fizzbuzz para ambos

for i in range(1, 101):
    if i % 3 == int() and i % 5 == int():
        print(i, 'fizzbuzz')
    elif i % 3 == int():
        print(i, 'fizz')
    elif i % 5 == int():
        print(i, 'buzz')
    else:
        print(i)