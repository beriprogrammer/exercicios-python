# Verifique se um número inteiro está dentro de um intervalo específico.

num = int(input("Digite um número: "))

num_inferior = 5
num_superior = 105

if num_inferior <= num <= num_superior:
    print(f"O número {num} está dentro do intervalo.")
else:
    print(f"O número {num} está fora do intervalo.")