# 45. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50\. 

# As formas 1 e 2 implementam de forma vertical

# FORMA 1 
# for numero in range(1, 51):
#     if numero % 2 != 0:
#         print(list(numero))


# FORMA 2
# for numero in range(1, 51, 2):
#     print(numero)







#As formas(4 e 3) a baixo implementam em forma de lista

# FORMA 3
numeros_impares = []

# Percorre os números de 1 a 50
for numero in range(1, 51):
    # Se o número for ímpar (o resto da divisão por 2 não é 0)
    if numero % 2 != 0:
        # Adiciona o número à lista
        numeros_impares.append(numero)

# Imprime a lista completa
print(numeros_impares)


# FORMA 4 
# A linha abaixo faz exatamente o que o loop da forma 1 faz
numeros_impares = [numero for numero in range(1, 51) if numero % 2 != 0]

print(numeros_impares)