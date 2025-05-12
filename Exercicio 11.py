'''Escreva um programa que leia 20 números inteiros, guarde em uma lista e, em seguida, calcule e
apresente:
a. a quantidade de números pares.
* Dica: o operador matemático % retorna o resto da divisão e um número par é um número
divisível por 2 . Assim, se você dividir um número par por dois, o resto será zero.
b. o menor elemento da lista;
c. a soma dos 10 primeiros elementos'''

lista = []
indice = 0
par = 0
menorNumero = float('inf')
soma = 0
resto = 0

while (indice < 20):
    numero = int(input("Digite um nimero inteiro: "))
    lista.append(numero)
    
    resto = lista[indice] % 2
    if (resto == 0):
        par += 1
    if (menorNumero > numero):
        menorNumero = numero
    if (indice < 10):
        soma = soma + lista[indice]
    
    indice = indice + 1
print(f"A quantidade de pares é: {par}")
print(f"O menor numero é: {menorNumero}")
print(f"A soma dos 10 primeiro é: {soma}")
    