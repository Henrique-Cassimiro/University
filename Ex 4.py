'''Foi feita uma pesquisa para determinar o índice de mortalidade infantil em um certo
período. Fazer um algoritmo que:
- Leia inicialmente o número de crianças nascidas no período;
- Leia, em seguida, um número indeterminado de linhas, contendo, cada uma, o
sexo de uma criança morta (feminino ou masculino) e o número de meses de vida
da criança. A última linha, que não entrará nos cálculos, contém um sexo inválido;
Determine e imprima:
a) a porcentagem de crianças mortas no período;
b) a quantidade de crianças que não chegou a completar um ano de vida;
c) a quantidade de crianças do sexo masculino mortas no período, que viveu um
ano ou mais.
'''

nascidas = int(input("Qual o número de crianças nascidas no período?\n"))
sexo = input("Digite o sexo da criança morta: \n")
contador_criança = 0
menor_um_ano = 0
criança_macho = 0

while (sexo == "feminino" or sexo == "masculino" ):
    
    meses_vida = int(input("Quantos meses ela viveu?\n"))  
    
    contador_criança += 1
    if (meses_vida < 12):
        menor_um_ano += 1
    if (meses_vida >= 12 and sexo == "masculino"):
        criança_macho += 1
    sexo = input("Digite o sexo da criança morta: \n")
        
    
porcentagem_mortas = contador_criança * (100 / nascidas)
print(f"A porcentagem de crianças mortas no periodo é {porcentagem_mortas}%")
print(f"{menor_um_ano} não chegram a completar um ano\n{criança_macho} são do sexo masculino e viveu mais de um ano")
    
     