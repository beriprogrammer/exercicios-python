semana_dia = []

for i in range(7): # O loop 'for' vai rodar 3 vezes (para i = 0, 1 e 2)
    try: 
        numero = int(input(f"Digite o {i+1}º número (de 1 a 7): ")) # pedir numero
        semana_dia.append(numero) # adiciona número a lista numeros
        if numero == 1:
            print("1 - Domingo")
        elif numero == 2:
            print("2 - Segunda")
        elif numero == 3:
            print("3 - Terça")
        elif numero == 4:
            print("4 - Quarta")
        elif numero == 5:
            print("5 - Quinta")
        elif numero == 6:
            print("6 - Sexta")
        elif numero == 7:
            print("7 - Sábado")
        else:
            print("Valor inválido. Por favor, digite um número entre 1 e 7.")
    except ValueError:
        print("O valor digitado não é um número")