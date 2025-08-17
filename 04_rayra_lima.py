valorSalarioHora = float(input("Digite o valor do salário por hora: "))
horasTrabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salarioBruto = valorSalarioHora * horasTrabalhadas

ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

totalDescontos = ir + inss + sindicato
salarioLiquido = salarioBruto - totalDescontos

print(f"Salário Bruto: R$ {salarioBruto:.2f}")
print(f"Desconto IR (11%): R$ {ir:.2f}")
print(f"Desconto INSS (8%): R$ {inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salarioLiquido:.2f}")