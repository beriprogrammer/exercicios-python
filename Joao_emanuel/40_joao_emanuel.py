salario_inicial = float(input("Digite o salário: "))
if salario_inicial <= 280.00:
    percentual_aumento = 20
elif salario_inicial <= 700:
    percentual_aumento = 15
elif salario_inicial <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5
valor_aumento = salario_inicial * (percentual_aumento / 100)
novo_salario = salario_inicial + valor_aumento


print(f"Salário antes do reajuste: R${salario_inicial}")
print(f"O funcionário teve um aumento de {percentual_aumento}%")
print(f"O valor do aumento foi de {valor_aumento:.2f}")
print(f"O valor do novo salário é de: R${novo_salario}")


