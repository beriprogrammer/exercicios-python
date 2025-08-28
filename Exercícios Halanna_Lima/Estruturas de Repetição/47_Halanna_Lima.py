# Realizar a sequência de fibonacci e mostrar ao usuário

a = 0
b = 1
valorTemporario = 0
qntdVezes = int(input("Digite quantos números você deseja que apareça na sequência de fibonacci: "))


for i in range(qntdVezes):
    print(a, end = ", ")
    valorTemporario = a
    a = b
    b = valorTemporario + b
