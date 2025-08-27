print("Calculadora de soma (inteiros)")
print("=============================================")
numOperacoes = int(input("Quantas operações você deseja fazer? "))
print("----------------------------------")
for i in range(numOperacoes):

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    soma = numero1 + numero2
    print("O resultado é: ", soma)
    print("----------------------------------")

print("=============================================")
