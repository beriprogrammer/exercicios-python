vel = float(input("Digite a velocidade do carro ao passar pelo radar em km/h: "))

if vel >= 55:
    if vel <= 60:
        print("Multa no valor de R$130,16, classificação média.")
    elif vel <= 75:
        print("Multa no valor de R$195,23, classificação grave.")
    else:
        print("Multa no valor de R$880,41, classificação gravíssima.")
else:
    print("Velocidade registrada não superior ao permitido na rodovia.")