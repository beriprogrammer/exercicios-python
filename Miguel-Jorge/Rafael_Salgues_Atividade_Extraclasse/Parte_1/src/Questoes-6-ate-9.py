numero = int(input('Insira numero inteiro: '))

if numero > 0:
    print('Numero é positivo')
elif numero < 0:
    print('Numero é negativo')
else:
    print('O numero é zero')

if numero % 2 == 0:
    print('Numero é par')
else:
    print('Numero é impar')