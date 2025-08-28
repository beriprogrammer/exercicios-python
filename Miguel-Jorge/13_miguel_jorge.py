numero = int(input("Digite um número inteiro: "))
# Define os limites do intervalo
limite_inferior = 10
limite_superior = 50

# A operação 'and' só será verdadeira se ambas as condições forem verdadeiras
if numero >= limite_inferior and numero <= limite_superior:
    print(f"O número {numero} está dentro do intervalo.")
else:
    print(f"O número {numero} não está dentro do intervalo.")
