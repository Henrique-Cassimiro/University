'''Faça um programa que leia 20 números inteiros, armazene-os em uma lista e imprima a lista.
Depois, armazene os números que estão em posições pares em uma lista chamada ‘listaA’ e os números que estão
em posições ímpares em uma lista chamada ‘listaB’. Imprima as duas listas criadas'''

lista = []
listaA = []
listaB = []
indice = 0

while (indice < 20):
    numero = int(input("Digite um nimero inteiro: "))
    lista.append(numero)
    indice += 1
    
print(lista)

indice = 0

while (indice < 20):
    if (indice % 2 == 0):
        listaA.append(lista[indice])
    else:
        listaB.append(lista[indice])
    indice += 1
print(f"posição par: {listaA} \nposição impar: {listaB}")