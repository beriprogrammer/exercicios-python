# Pedir quanto pescou no dia e calcular multa caso houver

pescaDiaria = float(input("Olá João quantos kg de peixe o senhor pescou hoje? "))
excesso = pescaDiaria - 50
valorMulta = excesso * 4

largura = 100
titulo = " CALCULAR MULTA KG/PEIXE "

print("-" * largura)
print("|" + titulo.center(largura - 2) + "|")
print("-" * largura)



if pescaDiaria > 50:
    print(f"|  Seu João você pescou {pescaDiaria:.2f} Kg hoje e excedeu os 50 kg em {excesso:.2f}KG portanto".ljust(largura - 1) + "|" )
    print(f"|  Irá pagar uma multa de: R$ {valorMulta:.2f}.""".ljust(largura - 1) + "|" )
else:
    print("|  A pesca de hoje não excedeu limite".ljust(largura - 2) + "|")
print("-" * largura)
