# Pedir um número e gerar a tabuada dele, além de mostrar ao usuário

numTabuada = int(input("Digite o número desejado  para que seja gerada a tabuada: "))

print(f"\nTabuada do {numTabuada}:\n")

for i in range(1, 11):
    resultado = numTabuada * i
    print(f"{numTabuada:2} x {i:2} = {resultado:3}")
