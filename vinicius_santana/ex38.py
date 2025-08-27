semana = int(input("informe um numero: "))

if semana % 7 == 1:
    print("domingo")
elif semana % 7 == 2:
    print("segunda")
elif semana % 7 == 3:
    print("terca")
elif semana % 7 == 4:
    print("quarta")
elif semana % 7 == 5:
    print("quinta")
elif semana % 7 == 6:
    print("sexta")
else:
    print("sabado")

