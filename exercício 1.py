'''Faça um programa que leia 6 números inteiros digitados pelo usuário e armazene em uma lista. Depois,
imprima:
a. cada elemento da lista individualmente, um em cada linha;
b. os 3 primeiros elementos;
c. a soma dos elementos pares'''

listaNumerica = []
indice = 0

while (indice < 6):
    numero = int(input("digite um número inteiros: "))
    listaNumerica.append(numero)
    indice += 1
    
soma = 0
cont = 0
indiceDaLista = 0
while (cont < 6):
    
    if (listaNumerica[indiceDaLista] % 2 == 0):
        soma = soma + listaNumerica[indiceDaLista]
    indiceDaLista += 1
    cont += 1
cont = 0   
while (cont < 6):
    print(listaNumerica[cont])
    cont += 1
print(listaNumerica[0], listaNumerica[1], listaNumerica[2])
print(f"A soma dos elemnetos pares é: {soma}")



