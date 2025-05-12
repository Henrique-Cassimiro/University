'''Suponha que você trabalha em uma loja de eletrodomésticos e precisa desenvolver um programa que ajude
a calcular o valor total de uma compra. O valor total da compra depende de alguns fatores, tais como a
quantidade de produtos comprados e o valor unitário de cada produto. Além disso, a loja oferece um desconto
de 10% para compras acima de R$ 1000,00'''

quantidade = int(input("Qual a quantidade de produtos comprados? "))
valor = float(input("Qual o valor unitário de cada produto? "))

valorTotal = quantidade * valor

if (valorTotal >= 1000):
    valorDesconto = valorTotal - (valorTotal * (10/100))
    print("O valor a ser pago é de: ", valorDesconto)
    
else:
    print("O valor a ser pago é de: ", valorTotal)
