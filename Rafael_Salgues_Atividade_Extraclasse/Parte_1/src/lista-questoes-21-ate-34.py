numerosPar = [10, 2, 4, 8, 6, 12]
numerosImpar = [1, 3, 5, 7, 9, 11 ]
numerosFlutuantes = [2.3, 5.6, 8.5, 10.5, 2.4, 1.7]
dobro_da_lista = [2,4,6,8]
lista_dobro =[]

Lista_frutas_01 = ['uva', 'maça', 'abacaxi', 'laranja']
lista_fruta_02 = ['pessego', 'morango', 'goiaba']

lista_frutas_unidas = Lista_frutas_01 + lista_fruta_02
print(lista_frutas_unidas)

for numero in dobro_da_lista:
    resultado = numero * 2
    lista_dobro.append(resultado)

print(numerosPar)
print(sum(numerosPar))
print(min(numerosPar))
print(max(numerosPar))
print(len(numerosPar))
numerosPar.sort()
print(numerosPar)
print(sorted(numerosPar,reverse=True))
lista_frutas_unidas.sort()
print(lista_frutas_unidas)
print(sorted(lista_frutas_unidas, reverse= True))
print(sum(numerosFlutuantes))
print(min(numerosFlutuantes))
print(lista_dobro)
