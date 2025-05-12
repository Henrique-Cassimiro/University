'''Escreva um algoritmo que leia três números e faça o seguinte:
Caso todos os números sejam diferentes de zero:
Apresente a mensagem “Todos os números são diferentes a zero”, e calcule o resultado a ser apresentado
para o usuário da seguinte forma:
• Se todos os números forem positivos: o resultado é o produto dos números;
• Se pelo menos um número for positivo: o resultado é a soma dos números;
• Se todos os números forem negativos: o resultado é a média dos números.
• Caso contrário, informe ao usuário que todos os números devem ser diferentes de zero'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if(numero1 != 0 and numero2 != 0 and numero3 != 0):
    print("Todos os números são diferentes a zero")
    
    if(numero1 > 0 and numero2 > 0 and numero3 > 0):
        resultado = numero1 *numero2 * numero3
        print("O produto dos números é: ", resultado)
    elif(numero1 > 0 or numero2 > 0 or numero3 > 0):
        resultado = numero1 + numero2 + numero3
        print("A soma dos números é: ", resultado)
    elif(numero1 < 0 or numero2 < 0 or numero3 < 0):
        resultado = (numero1 + numero2 + numero3) / 3
        print("A média dos números é: ", resultado)
else:
    print("Todos os números devem ser diferentes de zero")
    
