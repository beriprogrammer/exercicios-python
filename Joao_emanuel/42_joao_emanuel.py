'''
entradas: respostas das 5 perguntas
processamento: receber a quantidade de verdades
saidas: inocente ou suspeita ou cumplice ou assassino
'''
perguntas = ["Telefonou para vítima?",
             " Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima: ",
             "Já trabalhou com a vítima?"]
qtd_verdade = 0
for duvidas in perguntas:
   resposta = input(duvidas)
   if resposta == "sim":
       qtd_verdade +=1
if qtd_verdade <=1:
    print("Você é inocente!")
elif qtd_verdade == 2:
    print("Vocé um suspeito!")
elif qtd_verdade <=4:
    print("Você é cúmplice!")
elif qtd_verdade == 5:
    print("Você é o assassino!")
else:
    print("Você é inocente!")
print(qtd_verdade)