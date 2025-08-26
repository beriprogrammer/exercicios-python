horaTrabalhada = int(input("Digite o número de horas trabalhadas: "))
valorHora = float(input("Digite o valor da hora trabalhada: "))

salario = horaTrabalhada * valorHora
impostoRenda = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salarioLiquido = salario - (impostoRenda + inss + sindicato)


print(f"""
      
      Seu salário bruto é: {salario}

    ==============================================
                DETALHES DO SALÁRIO
    ==============================================
      Seu imposto de renda é: {impostoRenda:.2f}
      Seu INSS é: {inss:.2f}
      Seu sindicato é: {sindicato:.2f}
      Seu salário líquido é: {salarioLiquido:.2f}

    ==============================================

""")
