# Mostrar na tela apenas os números impares de 1 a 50

listaImpar = []

for i in range(1,50):
    if i % 2 == 1 :
        listaImpar.append(i)
    else:
        continue
print(listaImpar)
