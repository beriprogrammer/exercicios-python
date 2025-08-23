import math
velocidade_media = int(input('Digite o valor da velocidade: '))

distancia_KM = 120 

tempo_hora = distancia_KM / velocidade_media
minutos = tempo_hora * 60

print(f'O veiculo levou {math.ceil(minutos)} minuto(s) para percorrer os 120Km')