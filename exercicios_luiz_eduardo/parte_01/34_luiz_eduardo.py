# Crie uma lista que contenha o dobro de cada elemento de outra lista (por exemplo, se a lista 
# original for [2, 3, 4], a nova lista deve ser [4, 6, 8]).

lista = [int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: "))]
dobro = []

for num in lista:
    dobro.append(num*2)

print(dobro)