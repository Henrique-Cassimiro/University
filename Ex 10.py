preco_ingresso = float(input("Digite o preço do ingresso sem desconto: R$ "))
profissao = input("Digite a profissão da pessoa (estudante, professor, bombeiro, artista ou outra): ").lower()
idade = int(input("Digite a idade da pessoa: "))

desconto = 0

if profissao == "estudante" or profissao == "professor":
    desconto += preco_ingresso / 2
elif profissao == "bombeiro":
    desconto += 15
elif profissao == "artista":
    desconto += 10

if idade >= 60 or idade <= 10:
    desconto += 20

preco_final = preco_ingresso - desconto

print("R$", preco_final)