# Criar lista de números inteiros e mostrar o menor número da lista

listaNumerosInteiros = []

for i in range(5):
    listaNumerosInteiros.append(int(input("Digite um número para adicionar a lista: ")))

print(f"O menor de todos os números da lista é: {min(listaNumerosInteiros)}")