# Solicita um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se é positivo
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero == 0:
    print("O número é zero, que não é positivo nem negativo.")
else:
    print(f"O número {numero} é negativo.")
