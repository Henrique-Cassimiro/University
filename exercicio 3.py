'''Faça um programa que inicialize uma lista da seguinte forma
lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
Depois, imprima:
● o maior elemento
● a soma dos elementos positivos
● os 5 primeiros elementos
● a posição dos elementos pares
* O código deve funcionar adequadamente para outros valores'''

lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
maiorElemento = 0
cont = 0
elemnto = 0
soma = 0

while (elemnto < len(lista)):
    if (lista[elemnto] > maiorElemento):
        maiorElemento = lista[maiorElemento]
    if (lista[elemnto] >= 0):
        soma = soma + lista[elemnto]
    if (cont < 5):
        print(lista[elemnto])
    if (lista[elemnto] % 2 == 0):
        print(f"Ele é par e está na posição {elemnto}")
        
    elemnto += 1

