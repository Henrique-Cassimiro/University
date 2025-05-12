'''Faça um algoritmo que leia o preço, o nome do artista e a categoria (Escultura ou
Quadro) de um número indeterminado de obras que foram expostas em feira de
artes, sendo que a leitura deverá ser encerrada quando o usuário digitar um preço
menor ou igual a zero. Calcule e imprima:
a. o nome do artista da escultura mais cara, considerando que não houve
empate;
b. a categoria da obra mais barata'''



preço = float(input("Digite o preço da obra:\n"))
menorPreçoEscultura = 99999999
maiorPreço = 0
nomeMaior = ''
categoriaMenor = ''

while (preço > 0):

    nome = input("Digite o nome do artista: \n")
    categoria = input("Digite a categoria da obra:\n")
    if (menorPreçoEscultura > preço and categoria == "escultura"):
        nomeMaior = nome
    if (maiorPreço < preço):
        categoriaMenor = categoria
    
    
    preço = float(input("Digite o preço da obra:\n"))

print(f"O artista com a escultura mais cara é: {nomeMaior}\n A categoria da obra mais barata é: {categoriaMenor}")