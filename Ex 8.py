bebida = input("Qual bebida foi pedida?\n")
conta = 0
agua = 2
refrigerante = 3
suco = 4
contAgua = 0
contSuco = 0
contRefri = 0

while (bebida != "sair"):
    quantidade = int(input("Digite q quantidade:\n"))
    if (bebida == "agua"):
        conta = conta + (agua * quantidade)
        contAgua = contAgua + quantidade
    elif (bebida == "suco"):
        conta = conta + (suco * quantidade)
        contSuco = contSuco + quantidade
    else:
        conta = conta + (refrigerante * quantidade)
        contRefri = contRefri + quantidade
    bebida = input("Qual bebida foi pedida?\n")
        
print(f"A conta da mesa foi: {conta}")
print(f"Foi pedido {contAgua} aguas, {contSuco} sucos e {contRefri} refrigerantes")
        
                