idade = int(input("Digite a idade do paciente: "))
peso = float(input("Digite o peso do paciente em kg: "))

if idade >= 12:
    if peso <= 60:
        gotas = 30
    else:
        gotas = 40
else:
    if peso <= 10:
        gotas = 5
    elif peso <= 20:
        gotas = 10
    elif peso <= 30:
        gotas = 15
    else:
        gotas = 20

print("O paciente deve tomar {gotas} gotas por dose.")