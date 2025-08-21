import math

area = float(input("informe quantos metros quadrados da area a ser pintada: "))


litros= area/3

latas = math.ceil(litros/ 18)

preco_total = 80 * latas

print(f"quantidade de litros necessarios: {litros:.2f}")
print(f"quantidade de latas necessarias: {latas}")
print(f"preco qua vai gastar: {preco_total}")


