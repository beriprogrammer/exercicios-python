import math

print('\nxxx PAINT STORE xxx\n')

area = float(input('Area to be painted (m²): '))
coverage = 3
volume = area / coverage
volume_pain_can = 18
number_paint_cans = math.ceil(volume / volume_pain_can)
price_can = float(80)
total = price_can * number_paint_cans

print('ID',3*' ','Desc',5*' ', 'Uni',3*' ','Price',4*' ','Total')
print('0302',1*' ','Color', 4*' ',f'{number_paint_cans}X',3*' ',f'{price_can} RS',3*' ',f'{total} RS')
print()