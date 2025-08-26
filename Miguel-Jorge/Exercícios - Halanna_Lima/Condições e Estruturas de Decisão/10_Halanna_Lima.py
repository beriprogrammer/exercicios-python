# Verificar se um número inteiro é divisível por outro.

Num1 = int(input("Digite um número:"))
Num2 = int(input("Digite um outro número:"))
RestoDivisao = Num1 % Num2

if RestoDivisao == 0:
    print(f"O número {Num1} e o número {Num2} são divisivéis entre si")
else :
    print(f"O número {Num1} e o número {Num2} não são divisivéis entre si")
