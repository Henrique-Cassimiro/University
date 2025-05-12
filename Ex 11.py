preco_produto = float(input("Digite o preço do produto: R$ "))
valor_pago = float(input("Digite o valor que o cliente entregou: R$ "))

if valor_pago < preco_produto:
    falta = preco_produto - valor_pago
    print(f"VALOR INSUFICIENTE, falta R$ {falta:.2f} para completar o pagamento.")
elif valor_pago == preco_produto:
    print("VALOR EXATO, NÃO TEM TROCO.")
else:
    troco = valor_pago - preco_produto
    print("VALOR SUPERIOR, TEM TROCO de R$", troco)