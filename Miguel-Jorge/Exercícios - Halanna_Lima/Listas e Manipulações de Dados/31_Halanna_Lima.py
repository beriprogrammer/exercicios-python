# Pedir ao usuário que insira várias palavras e quando ele desistir mostrar a palavras ordenadas (Z-A)

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

print(f"As palavras adicionadas nessa lista em ordem alfabética inversa é: {sorted(listaString, reverse= True)}")
