num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

'''11 e 12'''
if num1 == num2:
    print('Os númenos são iguais')
if num1 != num2:
    print('Os números são diferentes')

'''10'''
calculo = num1 % num2

if calculo == 0:
    print('Primeiro número é divisel pelo segundo sem deixar resto')
else:
    print('Primeiro número não é divisel pelo segundo, sobrou resto')