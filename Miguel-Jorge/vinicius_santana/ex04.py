'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Líquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

ganha_hora = float(input("informe quanto ganha por hora: "))
horas_job = int(input("informe quantas horas vc trabalha por mes: "))

salario_bruto = ganha_hora * horas_job

imposto = salario_bruto * 0.11 
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

total = imposto + inss + sindicato

salario_liquito =   salario_bruto - total 

print(f""" 
salario bruto: {salario_bruto}
imposto: {imposto}
inss: {inss}
sindicato: {sindicato}
salario liquido: {salario_liquito}

""")
