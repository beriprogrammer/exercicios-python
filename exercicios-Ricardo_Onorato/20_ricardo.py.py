#20. Considere que uma rodovia possui 120km de comprimento. Implemente um programa em Python que receba a velocidade média de um veículo nesta rodovia e informe quantos minutos ele demorou para cruzar esta estrada.

distancia_km = 120
velocidade_kmh = float(input("Informe a velocidade em km/h: "))

if velocidade_kmh <= 0:
    print("erro! Em deslocamento, a velocidade não pode ser igual nem menor que 0. Informe a velocidade correta.")
else:
    tempo_horas = distancia_km / velocidade_kmh # o resultado vai ser em horas e ele quer em minutos então tem que miltiplicar por 60
    tempo_minutos = tempo_horas * 60 # como ele quer o tempo em minutos tem que converter multiplicanto  o resultado por 60(1h = 60min)
    print(f'''O tempo em horas será de : {tempo_horas:.2f} Horas.
já em minutos será de: {tempo_minutos:.2f} minutos''')
