#Conversor de C° para F° ou F° para C°

escolha = float(input('Se deseja fazer de C° para F° digite 1, se deseja o contrário digite 2: '))

if escolha == 1:
    temp = float(input('Digite a temperatura desejada: '))
    resultado = (temp * 1.8) + 32
    print(resultado)
elif escolha == 2:
    temp1 = float(input('Digite a temperatura desejada: '))
    resultado1 = (temp1 - 32) / 1.8
    print(resultado1)
else:
    print('Você digitou um número não valido')
