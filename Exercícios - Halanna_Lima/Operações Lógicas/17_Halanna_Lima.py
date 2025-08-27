# Receber duas respostas e realizar a operação lógica (XOR / OU Exclusivo)

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

if gostaSorvete != gostaCoxinha:
    print("Você gosta de um, mas não do outro! OU exclusivo(XOR) detectado 😄")
else:
    print("Ou você gosta dos dois... ou de nenhum! Isso não é XOR 😅")
