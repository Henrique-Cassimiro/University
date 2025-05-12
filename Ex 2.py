'''Escreva um algoritmo que leia os valores de dois lados adjacentes de uma figura geométrica e informe se
eles representam um quadrado perfeito ou um retângulo. Caso represente um retângulo, informe o
tamanho do maior lado.
*Quadrado perfeito é aquele que possui todos os lados iguais.'''

base1 = float(input("Digite o valor da base da primeira figura: "))
altura1 = float(input("Digite o valor da altura da primeira figura: "))

base2 = float(input("Digite o valor da base da segunda figura: "))
altura2 = float(input("Digite o valor da altura da segunda figura: "))

TestePrimeiro = (base1 + altura1) / 2
TesteSegundo = (base2 + altura2) / 2


    
if (TestePrimeiro == base1):
    
    if (TestePrimeiro == altura1):
    
        print("A primeira figura é um quadrado perfeito!")

else:
    print("A primeira  figura é um retângulo!")
        
if (TesteSegundo == base2):
    
    if (TesteSegundo == altura2):
    
        print("A segunda figura é um quadrado perfeito!")

else:
    print("A segunda  figura é um retângulo!")

