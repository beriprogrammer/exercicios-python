# 37. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

for i in range(3): # O loop 'for' vai rodar 3 vezes (para i = 0, 1 e 2)
    num = int(input(f"Digite o {i+1}º número: ")) # pedir numero
    numeros.append(num) # adiciona número a lista numeros
numeros.sort(reverse=True) # organiza a lista (numeros) em ordem decrescente

print("Os números em ordem decrescente são:", numeros) # imprime a lista numeros em ordem decrescente


