# Criar lista e pedir pra adicionar números quando a pessoa desistir de adicionar mostra todos os números da lista em ordem decrescente


listaNumerosInteiros = []
resposta = True

while resposta == True :
    listaNumerosInteiros.append(int(input("Digite algum número para adicionar a lista: ")))
    resposta = input ("Deseja continuar adicionando? (1-sim 2-não): ")

    if resposta == "1":
        resposta = True
        continue
    else:
        resposta = False

print(f"Os números adicionados nessa lista em ordem decrescente é: {sorted(listaNumerosInteiros, reverse = True)}")
