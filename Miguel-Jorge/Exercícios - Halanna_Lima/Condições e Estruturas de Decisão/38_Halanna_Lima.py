# Ler  um número e exiba o dia correspondente da semana. 

diaSemana = int(input("Digite o dia da semana que você quer saber: "))

if diaSemana % 7 == 1:
    print("Esse dia cairá no Domingo")
elif diaSemana % 7 == 2:
    print("Esse dia cairá na Segunda")
elif diaSemana % 7 == 3:
    print("Esse dia cairá na Terça")
elif diaSemana % 7 == 4:
    print("Esse dia cairá na Quarta")
elif diaSemana % 7 == 5:    
    print("Esse dia cairá na Quinta")
elif diaSemana % 7 == 6:
    print("Esse dia cairá na Sexta")
else:
    print("Esse dia cairá no Sábado")
