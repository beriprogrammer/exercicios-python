# Preencher duas listas e concatena-las

lista1 = []
lista2 = []

for i in range(3):
    lista1.append(str(input("Digite uma palavra para preencher a lista 1: ")))

for i in range(3):
    lista2.append(str(input("Digite uma palavra para preencher a lista 2: ")))

lista3 = lista1 + lista2
print(lista3)
