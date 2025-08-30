# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = [float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: ")), float(input("Nota 4: "))]
media = sum(notas) / len(notas)

print(f"A média entre as notas é: {media:.1f}")