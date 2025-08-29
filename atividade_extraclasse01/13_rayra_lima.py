num = int(input("Digite um número: "))
inicio_intervalo = int(input("Digite o início do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))

if inicio_intervalo <= num <= fim_intervalo:
    print(f"O número {num} está dentro do intervalo.")
else:
    print(f"O número {num} está fora do intervalo.")
