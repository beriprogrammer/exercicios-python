num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

condicao_A = num1 > 10
condicao_B = num2 % 2 == 0

print(f'\n--- Verificando com as condições: ---')
print(f'Condição A (num1 > 10): {condicao_A}')
print(f'Condição B (num2 é par): {condicao_B}\n')

resultado_and = condicao_A and condicao_B
print(f'Resultado de "A E B": {resultado_and}')

resultado_or = condicao_A or condicao_B
print(f'Resultado de "A OU B": {resultado_or}')

resultado_not_A = not condicao_A
print(f'Resultado de "NÃO A": {resultado_not_A}')

resultado_xor = condicao_A != condicao_B
print(f'Resultado de "A XOR B": {resultado_xor}')



