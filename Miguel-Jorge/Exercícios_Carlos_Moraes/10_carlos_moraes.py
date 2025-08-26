# Solicita os dois números inteiros
num1 = int(input("Digite o primeiro número inteiro (dividendo): "))
num2 = int(input("Digite o segundo número inteiro (divisor): "))

# Verifica se o divisor é diferente de zero
if num2 != 0:
    if num1 % num2 == 0:
        print(f"{num1} é divisível por {num2}.")
    else:
        print(f"{num1} não é divisível por {num2}.")
else:
    print("Erro: divisão por zero não é permitida.")
