# Solicita um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se é negativo
if numero < 0:
    print(f"O número {numero} é negativo.")
elif numero == 0:
    print("O número é zero, que não é negativo nem positivo.")
else:
    print(f"O número {numero} não é negativo.")
