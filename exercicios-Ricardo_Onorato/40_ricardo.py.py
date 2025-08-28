# 40. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.  
#     1. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:  
#     2. salários até R$ 280,00 (incluindo) : aumento de 20%  
#     3. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%  
#     4. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%  
#     5. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:  
#     6. o salário antes do reajuste;  
#     7. o percentual de aumento aplicado;  
#     8. o valor do aumento;  
#     9. o novo salário, após o aumento. 


try:
    # 1. Recebe o salário atual do colaborador
    salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

    # Inicializa as variáveis para o cálculo
    percentual_aumento = 0

    # 2. Determina o percentual de aumento com base no salário
    if salario_atual <= 280.00:
        percentual_aumento = 20
    elif salario_atual <= 700.00:
        percentual_aumento = 15
    elif salario_atual <= 1500.00:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    # 3. Calcula o valor do aumento e o novo salário
    valor_aumento = salario_atual * (percentual_aumento / 100)
    novo_salario = salario_atual + valor_aumento

    # 4. Informa na tela todos os detalhes
    print(f'''
--- Relatório de Aumento Salarial ---
Salário antes do reajuste: R$ {salario_atual:.2f}
Percentual de aumento aplicado: {percentual_aumento}%
Valor do aumento: R$ {valor_aumento:.2f}
Novo salário, após o aumento: R$ {novo_salario:.2f}''')

except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico para o salário.")