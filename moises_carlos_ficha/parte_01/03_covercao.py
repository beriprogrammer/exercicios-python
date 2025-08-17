
print("Conversão de metros para centimetros")
print("=============================================")

numDeOperacoes = int(input("Quantas conversões você deseja fazer? "))
print("----------------------------------")

for i in range(numDeOperacoes):
    metros = float(input("Digite a medida em metros: "))
    centimetros = metros * 100
    print(f"A medida em centímetros é:  {centimetros} cm")
    print("----------------------------------")

print("=============================================")