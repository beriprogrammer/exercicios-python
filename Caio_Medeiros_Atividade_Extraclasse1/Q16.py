num1 = int(input("Digite um numero inteiro para comparar com outros dois numeros: "))
num2 = int(input("Digite um numero inteiro a ser comparado: "))
num3 = int(input("Digite outro numero inteiro a ser comparado: "))

print(f"O numero {num1} é maior que {num2} ou maior que o numero {num3}? {num1 > num2 or num1 > num3}")