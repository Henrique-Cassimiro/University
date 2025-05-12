valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra < 100:
    desconto = 0
elif 100 <= valor_compra <= 500:
    desconto = 0.10  # 10% de desconto
else:
    desconto = 0.20  # 20% de desconto

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print("Valor final a ser pago: R$", valor_final)