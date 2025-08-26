# Pedir ao usuário que insira várias palavras e quando ele desistir mostrar a palavras ordenadas (A-Z)

listaString = []
resposta = True

while resposta == True :
    listaString.append(str(input("Digite alguma palavra para adicionar a lista: ")))
    resposta = input ("Deseja continuar adicionando? (1-sim 2-não): ")

    if resposta == "1":
        resposta = True
        continue
    else:
        resposta = False

print(f"As palavras adicionadadas nessa lista em ordem alfabética é: {sorted(listaString)}")
