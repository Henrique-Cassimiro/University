'''Faça um programa que leia números inteiros e guarde em uma lista, encerrando a entrada de dados
quando for digitado 0 (zero), que não deve ser armazenado.
Depois e imprima a lista criada, troque o sinal de todos os números (Ex. se o número for -5 troca por 5 ) e
imprima a lista novamente'''

lista = []
valor = int(input("Digite um valor [zero para encerrar]: "))

while (valor != 0):
    lista.append(valor)
    valor = int(input("Digite um valor [zero para encerrar]: "))
    
print(lista)

indice = 0
while (indice < len(lista)):
    lista[indice] = lista[indice] * -1
    indice += 1
    
print(lista)