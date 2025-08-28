#21. Crie uma lista com os números pares de 0 a 10\.

# try:
#     numero = int(input("Digite um número: "))

#     if numero % 2 == 0:
#         print(f"O número {numero} é par")
#     else:
#         print(f"O número {numero} não é par")

# except ValueError:
#     print("por favor, digite um numero inteiro.")



numeros_pares = []
for numero in range(0, 10):
    if numero % 2 == 0:
        numeros_pares.append(numero)


# lista = []

# numero = int(input("Digite um número"))

# for numero in lista