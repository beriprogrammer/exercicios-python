# Criar lista de números e realizar a soma de todos os números da lista

listaNumerosInteiros = []

for i in range(5):
    listaNumerosInteiros.append(int(input("Digite um número para adicionar a lista: ")))

print(f"A soma de todos os números da lista é: {sum(listaNumerosInteiros)}")
