'''Dados três valores A, B e C, verificar e informar se eles podem ser os comprimentos dos lados de um triângulo
e, se forem, verificar se compõem um triângulo equilátero, isósceles ou escaleno, sendo que:
- Triângulo é uma figura geométrica de três lados, onde cada lado é menor do que a soma dos outros
dois.
- Triângulo equilátero: três lados iguais.
- Triângulo isósceles: dois lados iguais.
- Triângulo escaleno: todos os lados diferentes.'''

ladoA = float(input("Digite o valor do primeiro lado: "))
ladoB = float(input("Digite o valor do segundoo lado: "))
ladoC = float(input("Digite o valor do terceiro lado: "))

verificaçãoA = ladoC + ladoB
verificaçãoB = ladoA + ladoC
verificaçãoC = ladoA + ladoB

if(ladoA < verificaçãoA and ladoB < verificaçãoB and ladoC < verificaçãoC):
    if(ladoA == ladoB and ladoB == ladoC):
        print("É um triangulo equilátero")
    elif((ladoA == ladoB or ladoB == ladoC or ladoC == ladoA) and ((ladoA != ladoB or ladoA != ladoC or ladoB != ladoC))):
       print("É um triangulo isóceles")
    else:
        print("É um triangulo escaleno")
       
    
else:
    print("Não é um triangulo possível!")

