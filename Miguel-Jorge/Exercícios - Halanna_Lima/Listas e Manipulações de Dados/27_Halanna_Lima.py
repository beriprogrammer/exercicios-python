# Criar lista e pedir pra adicionar elementos , quando a pessoa desistir de adicionar mostra o comprimento da lista

listaElementos = []
resposta = True

while resposta == True :
    listaElementos.append(input("Digite algo para adicionar a lista: "))
    resposta = input ("Deseja continuar adicionando? (1-sim 2-não): ")

    if resposta == "1":
        resposta = True
        continue
    else:
        resposta = False

print(f"A quantidade de elementos dessa lista é: {len(listaElementos)}")
