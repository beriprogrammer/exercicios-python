# Verificar se um número inteiro está dentro de um intervalo específico.

num1 = int(input("Digite um número: "))
inicioIntervalo = int(input("Insira o início do intervalo: "))
FimIntervalo = int(input("Insira o fim do intervalo: "))

if num1 >= inicioIntervalo and num1 <= FimIntervalo:
    print(f"O número {num1} está dentro do intervalo!")
else:
    print(f"O número {num1} está fora do intervalo")
