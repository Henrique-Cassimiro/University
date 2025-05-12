nome = input("Qual o seu nome completo??" )
email = input("Qual o seu email?" )
print("Parabéns, ", nome, "  Seu cadastro foi realizado com sucesso e você ganhou um cupom de desconto de 10% para a sua primeira compra na TecnoPlus.")
valorCompra = float(input("Qual o valor total da compra?"))
valorDesconto = (valorCompra/10)
valorFinal = valorCompra - valorDesconto
print("O valor total da sua compra é:", valorCompra, ". Com o cupom de desconto, voce tera um desconto de: ", valorDesconto, "o valor final a ser pago é: ", valorFinal)



