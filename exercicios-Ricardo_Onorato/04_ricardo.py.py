'''4.  Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no 
mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% 
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
a.  salário bruto. 
b.  quanto pagou ao INSS. 
c.  quanto pagou ao sindicato. 
d.  o salário líquido. 
calcule os descontos e o salário líquido, conforme a tabela abaixo: + Salário Bruto : R$ 
- IR (11%) : R$ 
- INSS (8%) : R$ 
- Sindicato ( 5%) : R$ 
= Salário Líquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.'''


ganhoPorHora = float(input("Iforme quanto você ganha por hora: "))
horasPorMes = float(input("informe o total de horas trabalhadas no mês: "))

salarioBruto = ganhoPorHora * horasPorMes

ir = 11/100 * salarioBruto
inss = 8/100 * salarioBruto
sindicato = 5 /100 * salarioBruto
descontos = ir + inss + sindicato

salarioLiquido = salarioBruto - descontos

print(f'''SALÁRIO BRUTO............R$ {salarioBruto}.
DESCONTOS:
INSS.....................R$ {inss}.
INPOSTO DE RENDA.........R$ {ir}.
SINDICATO................R$ {sindicato}.
SALÁRIO LÍQUIDO..........R$ {salarioLiquido}''')