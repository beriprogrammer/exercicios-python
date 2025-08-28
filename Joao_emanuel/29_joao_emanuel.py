lista = []
for i in range(5):
    lista.append(int(input("Adcione um numero: ")))
lista.sort(reverse=True)
print(f"A lista em ordem decrescente é {lista}")