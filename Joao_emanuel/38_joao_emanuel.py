dias_semana = {
    1:"Domingo",
    2:"Segunda",
    3:"Terça",
    4:"Quarta",
    5:"Quinta",
    6:"Sexta",
    7:"Sábado"
}
dia = int(input("Digite um numero: "))

if dia <= 7:
    print(f"{dias_semana[dia]}")
else:
    print("Número inválido")
