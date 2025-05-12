'''Faça um programa que inicialize uma lista da seguinte forma
lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
Depois, solicite ao usuário um número e, se ele existir na lista, informe quantas vezes ele aparece. Caso o
número não exista na lista, informe isso ao usuário.
* O código deve funcionar adequadamente para outros valores e outra quantidade de números'''

lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]

numeroUsuario = int(input("Digite um número: "))
repeticao = 0
cont = 0

if (numeroUsuario in lista):
    while (cont < len(lista)):
        if (numeroUsuario == lista[cont]):
            repeticao = repeticao + 1
        cont += 1
        
    print(f"O numero está na lista e aparece {repeticao} vezes")
else:
    print("O numero não está na lsita!")