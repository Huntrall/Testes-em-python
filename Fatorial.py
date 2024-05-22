#Fatorial fudido

num = float(input('Insira um número: '))

num1 = num

while num1 != 1:
    num1 = num1 - 1
    num = num1 * num

print(num)