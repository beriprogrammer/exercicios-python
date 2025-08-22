num1 = int(input("Digite o primeiro número inteiro (dividendo): "))
num2 = int(input("Digite o segundo número inteiro (divisor): "))

# Verifica se o divisor é diferente de zero
if num2 != 0:
    resto = num1 % num2
    print(f"O resto da divisão de {num1} por {num2} é {resto}.")
else:
    print("Erro: divisão por zero não é permitida.")
