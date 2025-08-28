# Pedir ao usuário que insira vários números e quando ele desistir mostrar os valores da lista e em seguida esse valor duplicado

listaNumero = []
resposta = True
listaNumeroDuplicada = []

while resposta == True :
    listaNumero.append(int(input("Digite algum número para adicionar a lista: ")))
    resposta = input ("Deseja continuar adicionando? (1-sim 2-não): ")

    if resposta == "1":
        resposta = True
        continue
    else:
        resposta = False

for i in listaNumero:
    listaNumeroDuplicada.append(i * 2)

print(listaNumero)
print(listaNumeroDuplicada)



