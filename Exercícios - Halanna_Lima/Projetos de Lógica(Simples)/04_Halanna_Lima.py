# Calcular salário bruto e logo em seguida o líquido a partir dos descontos

SalarioPorHora = float(input("Insira quanto você recebe por hora trabalhada: "))
HorasTrabalhadasMes = float(input("Insira quantas horas você trabalhou no mês: "))

SalarioBruto = SalarioPorHora * HorasTrabalhadasMes
ImpostoRenda = 0.11 * SalarioBruto
INSS = 0.08 * SalarioBruto
Sindicato = 0.05 * SalarioBruto
Desconto = ImpostoRenda + INSS + Sindicato
SalarioLiquido = SalarioBruto  - Desconto

largura = 100
titulo = " SALÁRIO DO MÊS "

print("-" * largura)
print("|" + titulo.center(largura - 2) + "|")
print("-" * largura)

print(f"|  Seu salário Bruto no mês é : R$ {SalarioBruto:.2f}".ljust(largura - 1) + "|" )
print(f"|  Valor INSS :R${INSS:.2f}".ljust(largura - 1) + "|")
print(f"|  Valor do importo de renda: R${ImpostoRenda:.2f}".ljust(largura - 1) + "|")
print(f"|  Valor Sindicato: R$ {Sindicato:.2f}".ljust(largura - 1) + "|")
print(f"|  Seu salário com todos os descontos é: R$ {SalarioLiquido:.2f}".ljust(largura - 1) + "|")
print("-" * largura)
