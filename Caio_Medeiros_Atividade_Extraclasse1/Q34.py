lista = [5.89, 4.21, 10.87, 7.44, 3.99, 11.37, 9.73]
lista_duplicada = []
print(lista)

for i in range(0, len(lista)):
    x = lista[i] * 2
    lista_duplicada.append(x)

print(f"Lista com valores duplicados: {lista_duplicada}")
