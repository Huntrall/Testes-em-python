#Tentando vericicar se uma palavra é um palíndromo :))

frase_usuario = str(input("Escreva uma palavra: "))

corretor_frase = frase_usuario.lower()

frase_invertida = corretor_frase[::-1]

if corretor_frase == frase_invertida:
    print("Sua frase é um palíndromo")
else:
    print("Sua frase não é um palíndromo")