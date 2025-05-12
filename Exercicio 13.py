'''Escreva um programa que leia as 10 respostas do gabarito de uma prova e guarde em uma lista G, sendo
que o índice representa o número da questão. A seguir, leia as 10 respostas de um aluno e guarde em uma
lista R. Imprima:
a. os números das questões que o aluno errou.
b. se o aluno foi aprovado ou reprovado, sendo que é aprovado o aluno que teve 6 ou mais acertos'''

listaG = []
indice = 0
gabarito = ''
erros = 0

while (indice < 10):
    gabarito = input("Digite o gabarito: ")
    listaG.append(gabarito)
    indice += 1
    
listaR = []
indice = 0
respota = ''

while (indice < 10):
    resposta = input("Digite a resposta do aluno: ")
    listaR.append(resposta)
    if (listaG[indice] != listaR[indice]):
        erros = erros + 1
    indice += 1
    
print(f"O aluno errou {erros} questões")
if (erros <= 4):
    print("aluno aprovado")
else:
    print("aluno reprovado")
