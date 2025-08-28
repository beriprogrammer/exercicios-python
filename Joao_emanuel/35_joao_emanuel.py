peso = float(input("Qual o peso do peixe em Kg: "))
excesso = peso - 50
multa = excesso * 4.00

if peso <= 50:
    print("-"*25)
    print(f"O peso do seu peixe foi de {peso}!")
    print(f"Você nao precisará pagar multa!")
    print("-" * 25)
else:
    print("-" * 25)
    print(f"O peso do peixe foi excedido em {excesso} Kg")
    print(f"Você pagará uma multa de R${multa}")
    print("-" * 25)