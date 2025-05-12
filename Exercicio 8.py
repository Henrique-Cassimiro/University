'''Faça um programa que leia 10 valores inteiros e armazene em um lista. Depois, troque o primeiro
elemento com o último'''

lista = []
contador = 0

while (contador < 10):
    valor = int(input("Digite um valor inteiro: "))
    contador += 1
    lista.append(valor)
    
primeiro = 0
ultimo = 0

primeiro = lista[0]
ultimo = lista[-1]

lista[0] = ultimo
lista[-1] = primeiro

print(lista)