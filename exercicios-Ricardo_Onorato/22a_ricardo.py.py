# 22. Crie uma lista com os números ímpares de 1 a 9\.

lista_impares = []

for numero in range(1, 9):
    if numero % 2 != 0:
        lista_impares.append(numero)

print(lista_impares)