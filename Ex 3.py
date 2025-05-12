'''Faça um programa que leia dois números e calcule a divisão do primeiro pelo segundo. Porém, se o usuário
digitar zero para o segundo número, não realize o cálculo e apresente uma mensagem de erro “Não pode
ser feita divisão por zero'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if (valor2 == 0):
    print("Não pode ser feito divisão por zero!")

else:
    divisão = valor1 / valor2
    print("A divisão do primeiro valor pelo segundo valor é: ", divisão)
    

