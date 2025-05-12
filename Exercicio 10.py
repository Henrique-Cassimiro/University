'''Escreva um programa que leia 10 números reais e guarde em uma lista, e:
a. imprima a lista;
b. troque os 5 primeiros números da lista pelo seu dobro;
c. troque os 5 últimos elementos da lista pela sua metade;
d. Imprima a lista novamente.'''

lista = []

indice = 0

while (indice < 10):
    numero = int(input("Digite um nimero inteiro: "))
    lista.append(numero)
    indice += 1
    

print(lista)

indice = 0
final = 1
while (indice < 5):
    lista[indice] = lista[indice] * 2
    indice += 1
    lista[len(lista) - final] = lista[len(lista) - final] / 2
    final += 1

print(lista)