# 35. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável *peso* (peso de peixes) e calcule o excesso. Gravar na variável *excesso* a quantidade de quilos além do limite e na variável *multa* o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_digitado = float(input("Informe o peso (Kg) dos peixes que você pescou: "))
peso_permitido = 50
excesso = peso_digitado - peso_permitido
multa = excesso * 4

if peso_digitado > 50:
    print(f'''
A quantidade pescada, ultrapassou a permitida em {excesso} kg
O valor da multa a ser pago será de: R$ {multa}''')
elif peso_digitado <= 50:
    print(f'''
A quantidade total pescada foi de: {peso_digitado} Kg
Você não pagará multa, porque está dentro do limite permitido de 50Kg''')
