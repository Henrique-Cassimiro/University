'''O código a seguir gera um valor inteiro aleatório (entre 0 e 10) e guarda em uma variável chamada
valorAleatorio:
import random
# Gerando um valor aleatório entre 1 e 10
valorAleatorio = random.randint(1, 10)
Continuando o código acima, após o programa gerar o valor aleatório, solicite ao usuário que digite um
número e, na sequência, informe se o número digitado pelo usuário é maior, menor ou igual ao valor
gerado aleatoriamente'''

import random
# Gerando um valor aleatório entre 1 e 10
valorAleatorio = random.randint(1, 10)

valorUsuario = int(input("Digite um valor inteiro entre 0 e 11: "))

if (valorUsuario == valorAleatorio):
    
    print("O valor é igual ao do computador!")
    
elif (valorUsuario > valorAleatorio):
    
    print("O valor é maior que o do computador!")
    
else:
    
    print("O valor é menor que o do computador!")
    
    