print("Escolha a opção:")
print("'so' - soma")
print("'su' - subtração")
print("'pr' - produto")
print("'di' - divisão")

opcao = input("Digite a opção desejada: ")

if opcao == "so" or opcao == "su" or opcao == "pr" or opcao == "di":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "so":
        resultado = num1 + num2
        print("Resultado da soma:", resultado)
    elif opcao == "su":
        if num1 > num2:
            resultado = num1 - num2
        else:
            resultado = num2 - num1
        print("Resultado da subtração:", resultado)
    elif opcao == "pr":
        resultado = num1 * num2
        print("Resultado do produto:", resultado)
    elif opcao == "di":
        if num2 == 0:
            print("Não pode ser feita divisão por zero!")
        else:
            resultado = num1 / num2
            print("Resultado da divisão:", resultado)
else:
    print("Opção inválida!")