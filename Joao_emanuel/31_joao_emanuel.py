lista = []

for i in range(5):
    lista.append(str(input("Digite algo: ")))
lista.sort(reverse=True)
print(f"A lista em ordem descrescente é {lista}")