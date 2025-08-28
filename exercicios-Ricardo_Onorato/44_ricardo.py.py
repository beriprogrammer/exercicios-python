'''44. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''


populacao_a = 80000
taxa_a = 0.03

populacao_b = 200000
taxa_b = 0.015

anos = 0

# enquanto  A for menor que B
while populacao_a < populacao_b:
    # A cada ano, calcula o crescimento de cada população
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    
    # Incrementa o contador de anos
    anos += 1

# Exibe o resultado final
print(f'''
A população do país A ultrapassará ou igualará a do país B em {anos} anos.
População final de A: {int(populacao_a)} habitantes.
População final de B: {int(populacao_b)} habitantes.''')