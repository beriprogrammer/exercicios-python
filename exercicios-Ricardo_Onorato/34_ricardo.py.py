# 34. Crie uma lista que contenha o dobro de cada elemento de outra lista (por exemplo, se a lista original for \[2, 3, 4\], a nova lista deve ser \[4, 6, 8\]).

precos = [2, 3, 4]
dobro_precos = []

for preco in precos:
    dobro = preco * 2
    dobro_precos.append(dobro)  # Adiciona o resultado à nova lista

print(dobro_precos)