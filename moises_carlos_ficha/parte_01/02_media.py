print("Calculadora de Média")
print("=============================================")
numDeNotas = int(input("Quantas notas você deseja calcular? "))
print("----------------------------------")
soma = 0
for i in range(numDeNotas):
    nota = float(input("Digite a nota: "))
    soma += nota
media = soma / numDeNotas
print("A média é: ", media)
print("=============================================")

# O exercicio pedia para calcular 4 notas, mas decidi ampliar as possibilidades
# para que o usuário possa calcular quantas notas quiser.