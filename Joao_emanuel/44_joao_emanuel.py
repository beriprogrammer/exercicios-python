'''
entrada: população pais A e população pais B
processamento: calcular o numero de anos necessário para que A iguale b
saida: escrever o numero de anos necessário para que o pais A iguale o país B
'''

paisA = 80000
taxaA= 0.03
paisB = 200000
taxaB = 0.015
anos = 0
while paisA < paisB:
    paisA = paisA + (paisA * taxaA)
    paisB = paisB + (paisB * taxaB)
    anos +=1
print(f"{paisA:.0f}")
print(f"{paisB:.0f}")
print(anos)
