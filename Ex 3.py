'''Numa fábrica trabalham homens e mulheres divididos em duas classes:
- A – os que fazem até 100 peças por mês;
- B – os que fazem mais de 100 peças por mês.
Os operários da classe ‘A’ recebem apenas o salário-mínimo mais 2.00 por peça e
os operários da classe ‘B’ recebem salário-mínimo mais R$ 2.50 por peça.
Fazer um algoritmo que:
1 - Leia inicialmente o valor do salário-mínimo;
2 - Leia várias linhas contendo o nome do operário e quantas peças ele fabricou no
mês. A última linha, que servirá de flag (condição de parada), terá o nome do
operário igual a “sair”.
3 - Apresente a folha de pagamento do mês, com as seguintes informações:
a. O nome, a classe e o salário de cada operário;
b. O valor do maior salário;
c. A somatória dos salários dos operários'''

salarioMinimo = float(input("Digite o valor do salario minimo:\n"))
nome = input("Digite o nome do operario:\n")
salarioFinal = 0
classe = ""
salarioMaior = 0
salarioSoma = 0

while (nome != "sair"):
    qntd_peças = int(input("Quantas peças esse operário fez?\n"))
    if (qntd_peças <= 100):
        classe = "A"
        salarioFinal = (qntd_peças * 2) + salarioMinimo 
    else:
        classe = "B"
        salarioFinal = (qntd_peças * 2.5) + salarioMinimo 
        
    if (salarioMaior < salarioFinal):
        salarioMaior = salarioFinal
    
    salarioSoma += salarioFinal
        
    print(f"O operário {nome} é da classe {classe} e seu salário é: {salarioFinal} ")
    nome = input("Digite o nome do operario:\n")
    
print(f"O maior salário foi de: {salarioMaior}\nA somatoria dos salarios foi de: {salarioSoma}")