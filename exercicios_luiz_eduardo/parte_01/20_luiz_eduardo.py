# Considere que uma rodovia possui 120km de comprimento. Implemente um programa em Python que receba a velocidade média de um veículo nesta rodovia e informe quantos minutos ele demorou para cruzar esta estrada.

distancia = 120
velocidade = float(input("Digite a velocidade média do veículo (km/h): "))
horas = distancia / velocidade
minutos = horas * 60

print(f"O veículo levou {minutos:.2f} minutos para cruzar a estrada.")