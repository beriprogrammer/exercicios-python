lista = []

for i in range(0, 3):
    n = float(input("Digite um numero para ser incluso na lista: "))
    lista.append(n)

lista.sort(reverse = True)
print(f"Lista dos valores em ordem decrescente: {lista}")