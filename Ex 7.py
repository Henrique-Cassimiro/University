'''A população de uma cidade cresce aproximadamente 10% ao ano. Faça um
programa que leia o ano atual e qual a população da cidade hoje e apresente qual é
a população estimada para cada ano até 2050.
Utilize a instrução while para resolver o problema.
Por exemplo, se o ano atual for 2022 e a população hoje for 1000:
2022 - 1000.00
2023 – 1100.00
2024 – 1210.00
... até 2050'''

ano_atual = int(input("Digite o ano atual:\n"))
populaçao_atual = int(input("Digite o população atual:\n"))

while (ano_atual < 2050):
    print(f"A polução atual é: {populaçao_atual} e o ano é: {ano_atual}")
    ano_atual += 1
    populaçao_atual = populaçao_atual + (populaçao_atual * 0.1)
    
print(f"A população em 2050 dessa cidade será: {populaçao_atual}")    