# 13. Verifique se um número inteiro está dentro de um intervalo específico.
try:
    lista = [7, 5, 3, 10, 4, 2, 6]

    numero = int(input("Informe o número: "))

    if numero in lista:
        print(f"O número {numero} consta ná lista")

    else:
        print(f"O número {numero} não consta ná lista")

except ValueError:
    print("Por favor, digitar núneros inteiros")