valorHoraTrabalho = int (input("Qual o  valor da hora trabalhada? "))
horaTrabalhada = int(input("Quantas horas trabalhasdas na semana? "))
desconto = float(input("Qual a porcentagem do desconto? "))
salarioB = (valorHoraTrabalho * horaTrabalhada) * 4.5
salarioD = salarioB - (salarioB * (desconto/100))

print("O salario bruto é: ", salarioB, " e o salario com desconto é: ", salarioD)
