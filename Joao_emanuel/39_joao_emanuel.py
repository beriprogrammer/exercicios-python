
velocidade_media = int(input("Digite a velocidade média em km/h: "))
if velocidade_media <= 55:
    print("Você não foi multado!")
    print("Boa viagem!")
elif velocidade_media <= 66:
    print("Você foi multado!")
    print("Sua infração é media!")
    print("O valor da sua multa é de R$130,16.")
elif velocidade_media < 83:
    print("Você foi multado!")
    print("Sua infração é grave!")
    print("O valor da sua multa é de R$195,23.")
else:
    print("Você foi multado!")
    print("Sua infração é gravíssima!")
    print("O valor da sua multa é de R$880,41.")