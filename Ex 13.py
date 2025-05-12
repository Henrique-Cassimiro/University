preco = float(input("Digite o preço do produto: R$ "))
condicao_pagamento = input("Escolha a condição de pagamento (dinheiro/cartão de débito, cartão de crédito à vista, 2x cartão de crédito ou 3x cartão de crédito): ").lower()

if condicao_pagamento == "dinheiro" or condicao_pagamento == "cartão de débito":
    desconto = preco * 0.10
    preco_com_desconto = preco - desconto
    print("O valor a ser pago à vista com 10% de desconto é: R$", preco_com_desconto)

elif condicao_pagamento == "cartão de crédito à vista":
    desconto = preco * 0.05
    preco_com_desconto = preco - desconto
    print("O valor a ser pago à vista no cartão de crédito com 5% de desconto é: R$", preco_com_desconto)

elif condicao_pagamento == "2x cartão de crédito":
    parcela = preco / 2
    print("O valor total a ser pago é: R$", preco)
    print("O valor de cada parcela é: R$", parcela)

elif condicao_pagamento == "3x cartão de crédito":
    juros = preco * 0.10
    preco_com_juros = preco + juros
    parcela = preco_com_juros / 3
    print("O valor total a ser pago com 10% de juros é: R$", preco_com_juros)
    print("O valor de cada parcela é: R$", parcela)

else:
    print("Condição de pagamento inválida!")
