'''42. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:  
    1. "Telefonou para a vítima?"  
    2. "Esteve no local do crime?"  
    3. "Mora perto da vítima?"  
    4. "Devia para a vítima?"  
    5. "Já trabalhou com a vítima?"   
       O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''


respostas_positivas = 0

perguntas = [
    "Telefonou para a vítima, sim ou não? ",
    "Esteve no local do crime, sim ou não? ",
    "Mora perto da vítima, sim ou não? ",
    "Devia para a vítima, sim ou não? ",
    "Já trabalhou com a vítima, sim ou não? "
]

# Loop faz todas as perguntas e conta as respostas positivas
for pergunta in perguntas:
    resposta = input(pergunta).strip().lower() # .strip() remove espaços e .lower() padroniza para minúsculas
    if resposta == "sim":
        respostas_positivas += 1

# Classifica o número de respostas positivas
if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")