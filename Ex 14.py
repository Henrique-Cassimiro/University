hora_entrada = int(input("Digite a hora de entrada (entre 10 e 22 horas): "))
hora_saida = int(input("Digite a hora de saída (entre 10 e 22 horas): "))

if hora_entrada < 10 or hora_entrada > 22 or hora_saida < 10 or hora_saida > 22:
    print("Erro: O estacionamento está aberto apenas entre 10 e 22 horas.")
elif hora_entrada >= hora_saida:
    print("Erro: A hora de entrada deve ser menor que a hora de saída.")
else:
    tempo_estacionamento = hora_saida - hora_entrada
    if tempo_estacionamento == 1:
        valor = 4.00
    elif tempo_estacionamento == 2:
        valor = 6.00
    else:
        valor = 6.00 + (tempo_estacionamento - 2) * 1.00

    print("O valor a ser pago pelo estacionamento é: R$", valor)
