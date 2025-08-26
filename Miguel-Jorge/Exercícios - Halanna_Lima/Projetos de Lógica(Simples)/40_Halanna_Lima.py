# Pedir ao colaborador que insira seu salário e calcular o reajuste

nomeColaborador = str(input("Digite seu nome: "))
salarioColaborador = float(input(f"Olá {nomeColaborador}, digite seu salário: R$ "))

if salarioColaborador <= 280.00:
    percentual = 20
elif salarioColaborador <= 700.00:
    percentual = 15
elif salarioColaborador <= 1500.00:
    percentual = 10
else:
    percentual = 5

reajusteSalario = salarioColaborador * (percentual / 100)
novoSalario = salarioColaborador + reajusteSalario

largura = 100
titulo = " REAJUSTE SALARIAL "

print("-" * largura)
print("|" + titulo.center(largura - 2) + "|")
print("-" * largura)

print(f"| Colaborador(a): {nomeColaborador}".ljust(largura - 1) + "|")
print(f"| Salário antes do reajuste: R$ {salarioColaborador:.2f}".ljust(largura - 1) + "|")
print(f"| Percentual de aumento aplicado: {percentual}%".ljust(largura - 1) + "|")
print(f"| Valor do aumento: R$ {reajusteSalario:.2f}".ljust(largura - 1) + "|")
print(f"| Novo salário após o aumento: R$ {novoSalario:.2f}".ljust(largura - 1) + "|")
print("-" * largura)
