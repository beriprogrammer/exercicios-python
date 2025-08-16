# Pedir a valocidade do carro e verificar se houve infração em relação ao limite de velocidade 

velocidadeCarro = int(input("Qual velocidade que o carro está?: "))

limite = 50
tolerancia = limite * 1.10  

largura = 100
titulo = " CALCULAR MULTA CARRO "

print("-" * largura)
print("|" + titulo.center(largura - 2) + "|")
print("-" * largura)


if velocidadeCarro <= limite:
    print("|  Nenhuma multa, parabéns por se comportar no trânsito!".ljust(largura - 1) + "|")
elif velocidadeCarro <= tolerancia:
    print("|  Velocidade excedida, mas dentro da tolerância de 10%. Nenhuma multa.".ljust(largura - 1) + "|")
else:
    excesso = velocidadeCarro - limite
    percentual_excesso = (excesso / limite) * 100

    print(f"|  Você excedeu o limite em {percentual_excesso:.2f}%.".ljust(largura - 1) + "|")

    if percentual_excesso <= 20:
        print("|  Infração MÉDIA - multa de R$ 130,16".ljust(largura - 1) + "|")
    elif percentual_excesso <= 50:
        print("|  Infração GRAVE - multa de R$ 195,23".ljust(largura - 1) + "|")
    else:
        print("|  Infração GRAVÍSSIMA - multa de R$ 880,41".ljust(largura - 1) + "|")

print("-" * largura)
