# Verifique se um número inteiro é divisível por outro.

num = int(input("Digite um número: "))
divisor = int(input("Digite o divisor: "))

if num % divisor == 0:
    print(f"O número {num} é divisível por {divisor}")
else:
    print(f"O número {num} não é divisível por {divisor}")