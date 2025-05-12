'''Uma companhia de saneamento calcula o valor da conta de água de acordo com o tipo de consumidor:
- Residencial: R$ 5.00 de taxa mais R$ 0.05 por m3 gasto;
- Comercial: R$ 500.00 para os primeiros 80 m3, acrescido de R$ 0.25 por m3 gastos acima dos 80 m3;
- Industrial: R$ 800.00 para os primeiros 100 m3, acrescido de R$ 0.04 por m3 gastos acima dos 100 m3.
Baseando-se nessas informações, escreva um algoritmo que leia o tipo do cliente e o seu consumo de água
em metros cúbicos. Depois, calcule e apresente a conta de água a ser paga pelo cliente'''

cliente = input("Declare seu perfil - r: para residencial, c: para comercial, i: para industrial:  ")
metrosCubicos = float(input("Digite o valor gasto em metros cúbicos: "))

valorResidencial = 5 + (0.05 * metrosCubicos)
valorComercial = 500 + (0.25 * metrosCubicos)
valorIndustrial = 800 + (0.04 * metrosCubicos)

if (cliente == "r"):
    
    print("A conta de água é: ", valorResidencial)
    
elif (cliente == "c"):
    
    print("A conta de água é: ", valorComercial)

else:
    
    print("A conta de água é: ", valorIndustrial)
