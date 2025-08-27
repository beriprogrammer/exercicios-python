import math

area = float(input("Digite o valor da área em metros quadrados que planeja utilizar a tinta: "))

litro = area / 3
lata = litro / 18



print(f"Quantidade de latas compradas será de: {math.ceil(lata)}")
print(f"O valor da lata de tinta é R$80,00, então gastará: R${math.ceil(lata) * 80}")