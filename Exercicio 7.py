'''Faça um programa que inicialize uma lista da seguinte forma
lista = [-5,10,-8,-3,5,10,11,8,-9,10]
Depois, armazene os números positivos da lista ‘números’ em uma lista chamada ‘positivos ’ e os números
negativos da lista ‘números’ em uma lista chamada ‘negativos’. Imprima as duas listas criadas.
* O código deve funcionar adequadamente para outros valores e outra quantidade de números'''

lista = [-5,10,-8,-3,5,10,11,8,-9,10]
positivos = []
negativos = []

indice = 0

while (indice < len(lista)):
    
    if(lista[indice] >= 0):
        positivos.append(lista[indice])
        
    else:
        negativos.append(lista[indice])
        
    indice += 1
        
print(f"positivos: {positivos}\n negativos: {negativos}")