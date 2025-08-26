valor_hora = float(input("Digite o valor do trabalho por hora: "))
horas = float(input("Digite o numero de horas trabalhadas no mes: "))

salario_bruto = valor_hora * horas
desconto_INSS = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_INSS - desconto_sindicato

print(f"O salario bruto foi de: {salario_bruto}")
print(f"Foi descontado para o INSS o valor de: {desconto_INSS}")
print(f"Foi descontado para o sindicato o valor de: {desconto_sindicato}")
print(f"O valor do salario liquido foi de: {salario_liquido}")
