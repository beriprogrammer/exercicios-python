# 23. Crie uma lista que contenha a concatenação de duas listas de strings.

recheios = []
molhos = []

print("Opções de recheio: milho, ervilha, azeitona, batata palha, frango, charque, carne de sol, frano com charque")
print("opções de molho: catchup, maionese, mostarda, catupyri, cheddar, barbequie")

for recheio in range(5):
    
    recheios.append(str(input(f"Escolha o recheio {recheio + 1} de 5: ")))

for molho in range(4):
   
    molhos.append(str(input(f"Escolha o molho {molho + 1} de 4: ")))

opcoes_completas = recheios + molhos

print(f'''Suas escolhas para recheio foram: {recheios}
Os molhos foram: {molhos}
Todas as opções escolhidas foram: {opcoes_completas}''')