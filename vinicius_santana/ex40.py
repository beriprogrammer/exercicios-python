def reajuste (salario):

    if salario <= 280.00:
        porcentagem = 20
    elif salario <= 700.00:
        porcentagem = 15
    elif salario <= 1500.00:
        porcentagem = 10
    else:
        porcentagem = 5

    aumento = salario * (porcentagem/100)
    salario_novo = salario + aumento
    print(f""" 
    \no salário antes do reajuste: {salario:.2f}
    \no percentual de aumento aplicado: {porcentagem}%
    \no valor do aumento: {aumento:.2f}
    \no novo salário, após o aumento: {salario_novo:.2f}
        """)
        
salario = float(input("informe seu  salario: "))

reajuste(salario)