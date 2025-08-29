import math

peso = float(input("Digite o valor em kg dos peixes pescados por João: "))

if 0 < peso <= 50:
    print(f"O peso não superou o limite estipulado pelo regulamento (50kg).")


elif peso > 50:
    excesso = peso - 50
    multa = math.ceil(excesso) * 4
    print(f"O peso pescado ultrapassou em {excesso}kg o valor permitido (50kg).")
    print(f"O valor da multa calculado ficou em: {multa}")

else:
    print("Valor incorreto. Programa finalizado.")
