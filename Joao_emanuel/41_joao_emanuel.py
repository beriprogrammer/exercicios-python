dias_mes = [0, 31,28,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
data_str = input("Digite uma data no formato dd/mm: ")
partes = data_str.split('/')
dia = int(partes[0])
mes = int(partes[1])


if 1 <= mes <= 12 and 1 <= dia <= dias_mes[mes]:
    if dia < 10:
        dia = f"0{dia}"
    if mes < 10:
        mes = f"0{mes}"
    print(f"A data {dia}/{mes} é válida para o ano de 2025")
else:
    print(f"A data {dia}/{mes} é inválida para o ano de 2025")

