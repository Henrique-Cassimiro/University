'''Um posto está com uma promoção, de forma que oferece os seguintes descontos, de acordo com a
quantidade abastecida:
● de 20 a 30 litros o desconto é de 5%; e
● acima de 30 litros o desconto é de 10%.
Elabore um algoritmo que leia a quantidade de litros e o tipo de combustível (A - Álcool ou G - Gasolina),
calcule e imprima o valor a ser pago, sabendo-se que o preço do litro da gasolina é de R$ 7.00 e o preço
do litro do álcool é de R$ 5.00'''

combustivel = input("Digite: a, para alcool e digite: g, para gasolina: ")
quantidade = float(input("Quantos litros foi abastecido: "))

valorAlcool = quantidade * 5
valorGasolina = quantidade * 7

if (combustivel == "a"):
    print("O valor do combustivel é: ", valorAlcool)
else:
    print("O valor do combustivel é: ", valorGasolina)
        
