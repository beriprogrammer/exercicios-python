# Verificar se um número inteiro é positivo.

numero = int(input("Digite um número: "))

if numero >= 1:
    print(f"O número inserido é {numero} e ele é positivo")
elif numero <= 0:
    print(f"O número inserido é {numero} e ele é negativo")
else :
    print("O numero digitado foi zero, ele é neutro")
