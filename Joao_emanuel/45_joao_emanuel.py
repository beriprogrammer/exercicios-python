'''
entrada: numero 0 e contador
processamento: calcular os numeros pares entre 1 e 50
saida: numeros pares entre 1 e 50
'''

numeros = 1
contador = 0
print("A sequência de números pares é: ")
while contador <=50:
    if numeros % 2 ==0:
        print(numeros)
    numeros +=1
    contador +=1
