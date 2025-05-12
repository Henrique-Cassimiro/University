'''Faça um algoritmo que leia um número e divida-o por dois (sucessivamente) até que
o resultado seja menor que 1. Mostre o resultado da última divisão e a quantidade
de divisões efetuadas'''

numero = float(input("Digite um número: "))
divisao = 99
cont = 0

while (divisao >= 1):
    
    divisao = numero/2    
    numero = divisao
    cont += 1
    
print(f"Houve {cont} divisões e o resultado da ultima divisão é: {divisao}")