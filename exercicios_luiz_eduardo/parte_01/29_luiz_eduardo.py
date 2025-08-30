# Crie uma lista com números inteiros e ordene-a em ordem decrescente.

numeros = [int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: "))]
decrescente = sorted(numeros, reverse=True)

print(f"Ordem decrescente: {decrescente}")