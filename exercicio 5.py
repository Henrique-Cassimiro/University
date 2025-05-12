'''Faça um programa que leia a média de 5 alunos e armazene em uma lista, calcule e apresente a média
geral da turma. Depois, apresente a quantidade de alunos com média maior que a média geral da turma'''

cont = 0
medias = []
mediasSomadas = 0
mediaGeral = 0
alunosMaiorQueAMedia = 0

while (cont < 5):
    media = float(input("Digite a media do alumo: "))
    medias.append(media)
    mediasSomadas = mediasSomadas + media
    cont += 1
    
mediaGeral = mediasSomadas / cont
print(f"A média é: {mediaGeral}")

elemento = 0
while (elemento < 5):
    if (medias[elemento] > mediaGeral):
        alunosMaiorQueAMedia += 1
    elemento += 1
print(f"São {alunosMaiorQueAMedia} que tiraram nota superior à média geral!")