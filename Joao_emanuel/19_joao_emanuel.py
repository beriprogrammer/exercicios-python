from math import ceil
metros = float(input("Digite o tamanho da área a ser pintada em metros: "))
litros = metros / 3
latas = ceil(litros / 18)
valor_lata = latas * 80

print(f"Para pintar {metros:.0f} metros, você precisará de {latas} latas que custará R${valor_lata:.2f}.")