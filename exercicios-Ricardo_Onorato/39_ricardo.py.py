# 39. Considere que o limite de velocidade da via é 50km/h. Implemente um programa que leia a velocidade que o carro passou do radar e informe o valor da multa e gravidade da punição (caso caiba a multa). Perceba que há uma tolerância de 10% para excesso de velocidade, ou seja, menos de 55km/h não leva multa.

# Definindo as constantes do limite e da tolerância
LIMITE_VELOCIDADE = 50  # em km/h
TOLERANCIA_PERCENTUAL = 10  # em %

# Calculando a velocidade limite com a tolerância
limite_com_tolerancia = LIMITE_VELOCIDADE * (1 + TOLERANCIA_PERCENTUAL / 100)

try:
    # Solicita a velocidade do carro
    velocidade_motorista = float(input("Digite a velocidade do carro (em km/h): "))

    # Verificando se o motorista está acima do limite com tolerância
    if velocidade_motorista <= limite_com_tolerancia:
        print("Você está dentro do limite de velocidade. Nenhuma multa será aplicada.")

    # Verificando o primeiro nível de multa (leve)
    elif velocidade_motorista > limite_com_tolerancia and velocidade_motorista <= LIMITE_VELOCIDADE * 1.2:
        multa_valor = 88.38
        print(f"Você foi multado por infração leve. Valor da multa: R$ {multa_valor:.2f}")

    # Verificando o segundo nível de multa (grave)
    elif velocidade_motorista > LIMITE_VELOCIDADE * 1.2 and velocidade_motorista <= LIMITE_VELOCIDADE * 1.5:
        multa_valor = 195.23
        print(f"Você foi multado por infração grave. Valor da multa: R$ {multa_valor:.2f}")

    # Verificando o terceiro nível de multa (gravíssima)
    else:
        multa_valor = 293.47
        print(f"Você foi multado por infração gravíssima. Valor da multa: R$ {multa_valor:.2f}")
        print("Punição: Suspensão do direito de dirigir.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número para a velocidade.")
