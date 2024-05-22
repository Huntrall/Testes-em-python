#Tentando fazer um programa que conte a vogal de uma frase e não me deixe maluco de vez
from unicodedata import normalize

frase_usuario = str(input("Digite uma frase: "))

frase_corrigida = normalize('NFKD', frase_usuario).encode('ASCII','ignore').decode('ASCII')

corretor_frase = frase_corrigida.lower()

contador_vogal = corretor_frase.count("a") + corretor_frase.count("e") + corretor_frase.count("i") + corretor_frase.count("o") + corretor_frase.count("u")

print("O número de vogais na sua frase é de: ", contador_vogal)
