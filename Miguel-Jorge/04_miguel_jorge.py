hora_ganha = float(input("Digite o quanto você ganha por hora: "))
hora_trabalhada = float(input("Digite o quanto você trabalha por mês: "))
imposto_renda = 0.11
inss = 0.08
sindicato = 0.05

total_mes = hora_ganha * hora_trabalhada
desconto_imposto = total_mes * imposto_renda
desconto_inss = total_mes * inss
desconto_sindicato = total_mes * sindicato
salario_liquido = total_mes - desconto_imposto - \
    desconto_inss - desconto_sindicato

print(f"Salário Bruto: R$ {total_mes:.2f}")
print(f"Desconto imposto de renda 11%: R$ {desconto_imposto:.2f}")
print(f"Desconto INSS 8%: R$ {desconto_inss:.2f}")
print(f"Desconto sindicato 5%: R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
