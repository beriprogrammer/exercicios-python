num1 = int(input("Digite um numero: "))
menor = int(input("Digite o menor valor do intervalo: "))
maior = int(input("Digite o maior valor do intervalo: "))

if num1 >= menor and num1 <= maior:
    print("Esse número está dentro do intervalo")
else:
    print(f"O número {num1} está fora do intervalo entre {menor} e {maior}")
