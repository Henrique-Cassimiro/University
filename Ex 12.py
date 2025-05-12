categoria = input("Digite sua categoria (Estudante, Professor ou Profissional): ")
minicurso = input("Deseja participar dos minicursos? (S para Sim ou N para Não): ")
traducao = input("Precisa de tradução simultânea? (S para Sim ou N para Não): ")

if categoria == "estudante" or categoria == "professor":
    valor_inscricao = 100.00
elif categoria == "profissional":
    valor_inscricao = 150.00
else:
    print("Categoria inválida!")
    exit()

if minicurso == "s":
    valor_inscricao += 50.00

if traducao == "s":
    valor_inscricao += 20.00

print("O valor da inscrição a ser pago é: R$" ,valor_inscricao)