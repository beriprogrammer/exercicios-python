'''19. Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

import math # inportar essa biblioteca para o math.ceil funcionar linha 12

tamanho = float(input("Informe o tamanho da área a ser pintada: "))

qtdLitros = tamanho * 18 / 54
qtdLatas = math.ceil(qtdLitros / 18) # math.ceil faz o arredondamento pra cima
precoTotal = qtdLatas * 80
print(qtdLatas)
print(precoTotal)

#1L de tinta pinta 3m(1L x 3m)
#uma lata com 18L(18L x 3m) pinta 54 metros
#cada lata custa R$ 80,00