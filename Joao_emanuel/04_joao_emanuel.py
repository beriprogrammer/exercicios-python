salarioh = float(input("Quanto você ganha por hora: R$ "))
horas = float(input("Quantas horas trabalhadas no mês: "))
salariob = salarioh * horas
imposto = salariob * (11/100)
inss = salariob * (8/100)
sindicato = salariob * (5/100)
salariol = salariob - (inss + imposto + sindicato)
print("-"*20)
print(f"Salário bruto: R${salariob}")
print(f"IR (11%): R${imposto}")
print(f"INSS (8%): R${inss}")
print(f"Sindicato (5%): R${sindicato}")
print(f"Salário líquido: R${salariol}")

