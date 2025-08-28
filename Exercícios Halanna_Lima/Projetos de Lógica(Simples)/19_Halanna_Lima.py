# Pedir a area, verificar quantas latas de tinta serão necessárias e dizer o valor

import math

AreaPraPintar = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
LitrosTintasGastos = AreaPraPintar / 3
QuantidadeLatasTinta = math.ceil(LitrosTintasGastos / 18) 
PrecoPorLata = 80

ValorTotal = QuantidadeLatasTinta * PrecoPorLata

largura = 100
titulo = " Loja de Tintas "

print("-" * largura)
print("|" + titulo.center(largura - 2) + "|" )
print("-" * largura)

print(f"|  Quantidade de latas a comprar: {QuantidadeLatasTinta}".ljust(largura - 1) + "|")
print(f"|  Preço total: R$ {ValorTotal:.2f}".ljust(largura - 1) + "|")
