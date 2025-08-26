# quebra uma linha, imprime sete espaços e o texto
from sympy.physics.units import centimeter

print('\n',5*' ','* M >> CM - Meters to centimeters converter *')

meters = float(input('\nMeters: '))

# Conversão de metros para centímetro
centimeters = round(meters * 100)

print(f'{meters} meters = {centimeters} Centimeters')

