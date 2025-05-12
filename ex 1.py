'''Faça um programa que leia a nota de 5 candidatos de um concurso e armazene em uma lista, calcule e apresente a
média das notas. Depois, apresente a quantidade de candidatos com a nota maior que a média.'''

notas = []
indice = 0
media = 0

while (indice < 5):
    nota = float(input("Digite a nota do candidato: "))
    notas.append(nota)
    media += nota
    indice += 1
media = media / len(notas)    
print(f"A media das notas é: {media}")

indice = 0
maiorMedia = 0
while (indice < len(notas)):
    if (notas[indice] > media):
       maiorMedia += 1 
    indice += 1
print(f"A quantidade de candidatos com notas maiores que a média é: {maiorMedia}")