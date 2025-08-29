x = int(input("Digite um valor inteiro correspondente a um dia da semana: "))

if x <= 7 and x > 0:
    if x == 1:
        print("Domingo")
    elif x == 2:
        print("Segunda-Feira")
    elif x == 3:
        print("Terça-Feira")
    elif x == 4:
        print("Quarta-Feira")
    elif x == 5:
        print("Quinta-Feira")
    elif x == 6:
        print("Sexta-Feira")
    else:
        print("Sábado")
else:
    print("Valor inválido.")