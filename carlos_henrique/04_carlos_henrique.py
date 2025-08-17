print('\n',4*' ','$ Accountant - Salary calculation\n')

currentMonth = input('Current month:')

hourlyWage = float(input('Hourly wage:'))

hoursPerMonth = float(input('Number of hours worked in the month: '))

# calculo do salário bruto, valor da hora de trabalho * total de horas trabalhadas por mês.
grossSalary = round((hourlyWage * hoursPerMonth),2)

# percentagem  de 8% do salário bruto para o inss
inss = round((grossSalary * 0.08),2)

# valor que representa 5% do salário bruto para o sindicato
union = round((grossSalary * 0.05),2)

# valor que representa 11% do salário bruto para o imposto de renda
icomeTax = round((grossSalary * 0.11),2)

# soma dos valores descontados do salário bruto
totalDeductions = round((inss + union + icomeTax),2)

# salário líquído
netSalary = round((grossSalary - totalDeductions),2)

print('\nCurrent month[', currentMonth,']')
print('Gross salary', 12*'.', grossSalary, 'R$')
print('INSS(8%)', 16*'.', inss, 'R$')
print('Union(5%)', 15*'.', union, 'R$')
print('Icome tax(11%)', 10*'.', icomeTax, 'R$')
print('\nNet salary', 14*'.', netSalary, 'R$')
