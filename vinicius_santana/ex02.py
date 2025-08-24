'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''


nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))
nota3 = float(input("informe a terceira nota: "))
nota4 = float(input("informe a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma/4

print(f"a media do aluno: {media}")