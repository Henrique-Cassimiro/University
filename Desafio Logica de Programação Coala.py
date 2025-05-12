'''João, um dos programadores da nossa equipe, é um coala disfarçado de humano, que passa 2/3
(16 horas) de seu dia dormindo. Assim, ele tem dificuldade em se organizar e concluir as suas atividades.
Para ajuda-lo faça um programa que receba 3 atividades que João tem que fazer no dia, lendo o nome da
atividade e o número de horas que ela ocupará, e:
● se der tempo de João fazer as 3 tarefas e dormir o suficiente,
avise-o disso;
● se não der, verifique se caso ele não faça a tarefa que ocupa o
menor número de horas, conseguirá fazer as outras duas. Se ele
conseguir, diga-o para ignorar a menor tarefa;
● se não conseguir, verifique se ele conseguirá fazer as duas
tarefas que ocupam menos tempo caso ignore a que demanda
maior tempo. Se sim, informe-o disso;
● Se não for possível, mande-o escolher qual delas deseja fazer e
dormir o resto do dia.'''

primeiraAtv = input("Digite o nome da primeira atividade: ")
primeiraAtvTempo = float(input("Quanto tempo a segunda atividade leva: "))
segundaAtv = input("Digite o nome da segunda atividade: ")
segundaAtvTempo = float(input("Quanto tempo a segunda atividade leva: "))
terceiraAtv = input("Digite o nome da terceira atividade: ")
terceiraAtvTempo = float(input("Quanto tempo a terceira atividade leva: "))

tempoTotal = primeiraAtvTempo + segundaAtvTempo + terceiraAtvTempo

if (tempoTotal <= 8):
    
    print("João, há tempo de concluir as atividades ",primeiraAtv,", ",segundaAtv,"e", terceiraAtv," e dormir!")
    
elif (tempoTotal > 8):
    
    
    
    if(primeiraAtvTempo < segundaAtvTempo and primeiraAtvTempo < terceiraAtvTempo):
        tempoCombinado = segundaAtvTempo + terceiraAtvTempo
        if (tempoCombinado <= 8):
            print("João, faça a atividade de: ", segundaAtv, " e ", terceiraAtv, " e não faça a atividade de: ", primeiraAtv)
    elif(segundaAtvTempo < primeiraAtvTempo and segundaAtvTempo < terceiraAtvTempo):
        tempoCombinado = primeiraAtvTempo + terceiraAtvTempo   
        if (tempoCombinado <= 8):
            print("João, faça a atividade de: ", primeiraAtv, " e ", terceiraAtv, " e não faça a atividade de: ", segundaAtv)
    elif(terceiraAtvTempo < primeiraAtvTempo and terceiraAtvTempo < segundaAtvTempo):
        tempoCombinado = primeiraAtvTempo + segundaAtvTempo
        if (tempoCombinado <= 8):
            print("João, faça a atividade de: ", primeiraAtv, " e ", segundaAtv, " e não faça a atividade de: ", terceiraAtv)

    elif (primeiraAtvTempo > segundaAtvTempo and primeiraAtvTempo > terceiraAtvTempo):
        tempoCombinado = segundaAtvTempo + terceiraAtvTempo
        if (tempoCombinado <= 8):
            print("João, faça a atividade de: ", segundaAtv, " e ", terceiraAtv, " e não faça a atividade de: ", primeiraAtv)
            
    elif (segundaAtvTempo > primeiraAtvTempo and segundaAtvTempo > terceiraAtvTempo):
        tempoCombinado = primeiraAtvTempo + terceiraAtvTempo
        if (tempoCombinado <= 8):
            print("João, faça a atividade de: ", primeiraAtv, " e ", terceiraAtv, " e não faça a atividade de: ", segundaAtv)
            
    elif (terceiraAtvTempo > primeiraAtvTempo and terceiraAtvTempo > segundaAtvTempo):
        tempoCombinado = primeiraAtvTempo + segundaAtvTempo
        if (tempoCombinado <= 8):
            print("João, faça a atividade de: ", primeiraAtv, " e ", segundaAtv, " e não faça a atividade de: ", terceiraAtv)
            
    else:
        print("Escolha uma única atividade para fazer e durma o resto do dia!")
       

    
    
        
    


