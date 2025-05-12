'''FAÇA UM PROGRAMA QUE LEIA A QUANTIDADE INDEFINIDA DE NÚMEROS E ARMAZENE EM UMA
LISTA, O PROGRAMA DEVE PARAR A LEITURA QUANDO O USUÁRIO DIGITAR 0 ZERO (FLAG). APRESENTE
A LISTA. APRESENTE CADA ELEMENTO INDIVIDUALMENTE UM POR LINHA APÓS A LEITURA E
PREENCHIMENTO DA LISTA'''

numero = int(input("Digite um número: "))
lista = []

contador = 0

while (numero != 0):
    contador += 1
    lista.append(numero)    
    numero = int(input("Digite um número: "))
    
cont = 0
while (cont < contador):
    
    print(lista[cont])
    cont += 1