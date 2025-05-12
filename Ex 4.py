''' Escreva um algoritmo que leia um número inteiro. Caso o número digitado seja par e positivo calcule e
apresente como resultado a metade deste número. Caso contrário, apresente como resultado o dobro do
número.
Dica: um número par é um número que é divisível por 2, ou seja, quando dividido por 2, retorna o resto igual a
0 (zero). Em um programa, para verificar se um número é par, pode-se usar operador módulo %, que retorna o
resto da divisão entre dois números'''

numero = int(input("Digite um número inteiro: "))
resto = numero % 2

if (resto == 0 and resto > 0):
    numero = numero / 2
    print(numero)
else:
    numero = numero * 2
    print(numero)

    