'''Faça um programa que leia e guarde em uma lista um número indeterminado de palavras, encerrando a
entrada de dados quando for informada a palavra “sair”, que não deve ser armazenada.
Depois da leitura, solicite ao usuário uma palavra e troque todas as ocorrências dela pela palavra
‘ELIMINADA’. Caso a palavra escolhida não exista na lista, informe isso ao usuário'''

palavra = input("Digite uma palavra [sair para encerrar]: ")
lista = []
cont = 0

while (palavra != "sair"):
    
    lista.append(palavra)
    palavra = input("Digite uma palavra [sair para encerrar]: ")
    cont += 1
    
palavra = input("digite uma palavra para eliminar da lista: ")
indice = 0
if (palavra not in lista):
    print("A palavra não está na lista!")
while (cont > 0):
    if (lista[indice] == palavra):
        lista[indice] = "ELIMINADA"
    indice += 1
    cont -= 1

print(lista)
        