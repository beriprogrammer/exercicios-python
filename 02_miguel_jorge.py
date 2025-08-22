notas = []
nota1 = int(input("Insira a nota do 1ª Bimestre: "))
notas.append(nota1)
# O método .append() é uma função de listas
# em Python que serve para adicionar um novo item no final de uma lista.
nota2 = int(input("Insira a nota do 2ª Bimestre: "))
notas.append(nota2)

nota3 = int(input("Insira a nota do 3ª Bimestre: "))
notas.append(nota3)

nota4 = int(input("Insira a nota do 4ª Bimestre: "))
notas.append(nota4)

soma = sum(notas)

media = soma / len(notas)

print(f"As notas inseridas foram: {notas}")
print(f"A média final foi: {media}")
