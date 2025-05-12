peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura ** 2)

print("O seu IMC é: ", round(imc, 2))

if imc < 18.5:
    print("Situação: Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Situação: Peso normal")
elif 25.0 <= imc <= 29.9:
    print("Situação: Sobrepeso")
elif 30.0 <= imc <= 34.9:
    print("Situação: Obesidade grau 1")
elif 35.0 <= imc <= 39.9:
    print("Situação: Obesidade grau 2")
else:
    print("Situação: Obesidade grau 3")