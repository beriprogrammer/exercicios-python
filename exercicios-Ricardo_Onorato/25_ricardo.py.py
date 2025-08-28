# 25. Crie uma lista com números inteiros e encontre o valor mínimo.

lista_precos = []

for i in range(10):

    valor = int(input(f"Informe o valor da sua proposta: "))
    lista_precos.append(valor)

print(f"A proposta com o melhor valor dessa licitação foi: {(min(lista_precos)):.2f}")