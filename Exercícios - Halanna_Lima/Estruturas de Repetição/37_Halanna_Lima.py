# pedir ao usuário para inserir números em uma lista e mostrar esses números em ordem decrescente

numeros = []
for i in range(3):
    numero = int(input(f"Digite o {i+1}º número para a lista: "))
    numeros.append(numero)

numeros.sort(reverse = True)
print(f"Lista em ordem Decrescente : {numeros}")