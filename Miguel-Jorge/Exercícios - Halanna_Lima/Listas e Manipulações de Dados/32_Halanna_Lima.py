# Pedir ao usuário que insira vários números decimais e quando ele desistir mostrar a soma dos números

listaNumeroDecimal = []
resposta = True

while resposta == True :
    listaNumeroDecimal.append(float(input("Digite algum número com casa decimal para adicionar a lista: ")))
    resposta = input ("Deseja continuar adicionando? (1-sim 2-não): ")

    if resposta == "1":
        resposta = True
        continue
    else:
        resposta = False
        
print(f"A soma de todos os números com casas decimais dessa lista é: {sum(listaNumeroDecimal)}")
