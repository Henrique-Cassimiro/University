'''Faça um programa que solicite ao usuário que digite um valor para a variável num. Verifica o número
digitado e informa se o é positivo, negativo ou zero. Caso o número seja positivo, apresente o seu dobro.
Caso o número seja negativo, informe se ele é par ou ímpar'''

num = float(input("Digite o valor: "))

if (num == 0):

    print("O número é zero")
    
elif (num > 0):
    
    dobro = num * 2
    print("O dobro do valor é: ", dobro)
    
else:
    restoNum = num % 2
    if ( restoNum == 0):
        print("É um número negativo e par")
    else:
        print("É um número negativo e ímpar")
        

