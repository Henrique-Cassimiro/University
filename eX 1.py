'''Faça um algoritmo que leia o sexo (‘F’ – Feminino ou ‘M’ – Masculino) e o turno de um aluno (‘M’ –
Matutino ou ‘V’ – Vespertino) e apresente uma das mensagens a seguir:
- “Bom dia, querida!”
- “Bom dia, querido!”
- “Boa tarde, querida!”
- “Boa tarde, querido!”'''

print("Digite F para feminino e M para masculino")
genero = input("Qual o gênero? ")
turno = input("Qual o turno do aluno? ")

if (genero == "M" and turno == "M"):
    
    print("Bom dia, querido!")
    
if (genero == "F" and turno == "M"):
    
    print("Bom dia, querida!")
    
if (genero == "M" and turno == "V"):
    
    print("Bom tarde, querido!")
    
if (genero == "F" and turno == "V"):
    
    print("Bom tarde, querida!")
    

