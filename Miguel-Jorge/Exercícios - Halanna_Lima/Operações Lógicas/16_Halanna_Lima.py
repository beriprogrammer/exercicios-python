# Receber duas respostas e realizar a operação lógica (OU)

gostaSorvete = input("Você gosta de sorvete? (1 - sim, 2 - não): ")

while gostaSorvete not in ['1', '2']:
    print("Entrada inválida. Por favor, insira 1 para sim ou 2 para não.")
    gostaSorvete = input("Você gosta de sorvete? (1 - sim, 2 - não): ")

if gostaSorvete == '1':
    gostaSorvete = True
else:
    gostaSorvete = False

gostaCoxinha = input("Você gosta de coxinha? (1 - sim, 2 - não): ")
while gostaCoxinha not in ['1', '2']:
    print("Entrada inválida. Por favor, insira 1 para sim ou 2 para não.")
    gostaCoxinha = input("Você gosta de coxinha? (1 - sim, 2 - não): ")

if gostaCoxinha == '1':
    gostaCoxinha = True
else:
    gostaCoxinha = False

if gostaSorvete or gostaCoxinha:
    print("Você gosta de pelo menos uma dessas delícias!")
else:
    print("Pelo visto você não gosta nem de coxinha nem de sorvete, que pessimo gosto.")
