#tentando criar um programa para calcular IMC

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

IMC = peso/altura**2

#IMC_L = round(IMC, 2)

if IMC < 18.5:
    print("Abaixo do peso", round(IMC, 2))
elif IMC >= 18.5 and IMC < 24.9:
    print("Peso normal", round(IMC, 2))
elif IMC >= 25 and IMC < 29.9:
    print("Sobrepeso", round(IMC, 2))
elif IMC >= 30 and IMC < 34.9:
    print("Obesidade Grau 1", round(IMC, 2))
elif IMC >= 35 and IMC < 39.9:
    print("Obesidade Grau 2", round(IMC, 2))
elif IMC >= 40:
    print("Obesidade Grau 3", round(IMC, 2))