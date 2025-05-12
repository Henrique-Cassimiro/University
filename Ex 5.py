'''Escreva um algoritmo que informe se um número digitado está compreendido entre 10 e 50, inclusive os
dois. Caso não esteja no intervalo indicado, informe se o número vem antes ou depois deste'''

numero = int(input("Digite um valor inteiro: "))

if(numero > 9 and numero < 51):
    print("O número está compreendido entre 10 e 50")
elif(numero < 10 ):
    print("O numero é menor que 10")
else:
    print("O número é maior que 50")
