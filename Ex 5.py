'''Ler dois valores e um código de condição. Se o código for “c” os valores devem ser escritos em ordem
crescente. Se o código for “d”, deve-se escrevê-los em ordem decrescente'''

valor1 = int(input("Entre com o primeiro valor: "))
valor2 = int(input("Entre com o segundo valor: "))
codigo = input("Digite se o código é: d, ou se o código é: c: ")

if (codigo == "c"):
    if ( valor1 > valor2):
        print(valor2 , valor1)
    else:
        print(valor1, valor2)
        
else:
    if (valor1 > valor2):
        print(valor1, valor2)
    else:
        print(valor2, valor1)
