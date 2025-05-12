''' Faça um programa que leia dois números, calcule e imprima a soma. Caso a soma seja par, calcula e
imprime a metade da soma'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

print("A soma dos numeros é: ", soma)

resto = soma % 2

metadeSoma = soma / 2

if (resto == 0):
    print("a metade da soma é: ", metadeSoma)
else:
    print("A soma não é par")