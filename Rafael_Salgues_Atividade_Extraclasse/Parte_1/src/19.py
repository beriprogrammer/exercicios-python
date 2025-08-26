import math

metrosQuadrados = int(input('Digite a area em M²: '))

quant_litros = metrosQuadrados / 3
quant_latas = quant_litros / 18 

precoFinal = quant_latas * 80

print(f"Para pintar {metrosQuadrados} M2 é necessário {math.ceil(quant_latas)} latas de tinta \n")
print(f"O valor final é de R$ {math.ceil(precoFinal)}")