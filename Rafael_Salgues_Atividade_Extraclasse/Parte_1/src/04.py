valorPorHora = float(input('Insira o valor ganho por hora: '))
horasTrabalhadas = float(input('Insira o valor de horas trabalhadas no mês: '))

salarioBruto = valorPorHora * horasTrabalhadas

imposto_de_renda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - (imposto_de_renda + inss + sindicato)

print(f'+ Salário Bruto: R$ {salarioBruto:.2f}')
print(f'- Imposto de Renda (11%): R$ {imposto_de_renda:.2f}')
print(f'- INSS (8%): R$ {inss:.2f}')
print(f'- Sindicato (5%): R$ {sindicato:.2f}')
print(f'= Salário Líquido: R$ {salarioLiquido:.2f}')
