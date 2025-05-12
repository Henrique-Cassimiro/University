'''Crie um programa que solicite ao usuário o nome dos funcionários e os salários de
cada uma deles e devolva a média, o salário mais alto e o salário mais baixo. Use
nome do funcionário = “fim” para encerrar a leitura.'''

nome = input(f"Digite o nome do funcionário: \n")
#salario = float(input("Digite o salário do funcionário:\n"))
salarioTotal = 0
salarioMaior = 0
salarioMenor = 9999999
cont = 0

while (nome != "fim"):
    cont += 1
    
    salario = float(input("Digite o salário do funcionário:\n"))
    
    salarioTotal += salario
    if (salarioMaior < salario):
        salarioMaior = salario
    if (salarioMenor > salario):
        salarioMenor = salario

    nome = input(f"Digite o nome do funcionário: \n")
    

media = salarioTotal / cont
print(f"A média dos salários é {media}\nO salário mais alto é {salarioMaior}\nO salário mais baixo é: {salarioMenor}")

