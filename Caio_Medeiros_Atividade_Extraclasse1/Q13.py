num1 = int(input("Digite o menor numero inteiro do intervalo: "))
num2 = int(input("Digite o maior numero inteiro do intervalo: "))

lista = list(range(num1, num2 + 1))

num3 = int(input("Digite um numero inteiro: "))

print(f"O numero {num3} esta contido no intervalo? {num3 in lista}")