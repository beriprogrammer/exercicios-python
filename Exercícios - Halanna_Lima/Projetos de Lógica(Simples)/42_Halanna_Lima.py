# Calcular o nível suspeito a partir e 5 perguntas 

largura = 100
titulo = " INVESTIGATÓRIO CRIMINAL "

print("-" * largura)
print("|" + titulo.center(largura - 2) + "|")
print("-" * largura)

nivelSuspeito = 0
perguntas = [
    "Por acaso você telefonou para a vítima? (1-sim 2-não): ",
    "Você esteve no local do crime? (1-sim 2-não): ",
    "Moras perto da vítima? (1-sim 2-não): ",
    "Devia alguma quantia para a vítima? (1-sim 2-não): ",
    "Já trabalhou com ou para a vítima? (1-sim 2-não): "
]

for pergunta in perguntas:
    print("| " + pergunta.ljust(largura - 3) + "|")
    
    resposta = input("> ")
    
    if resposta == "1":
        nivelSuspeito += 1

print("-" * largura)

if nivelSuspeito == 2:
    print("|  Você é suspeito, continuaremos a investigação amanhã".ljust(largura - 1) + "|")
elif nivelSuspeito == 3 or nivelSuspeito == 4:
    print("|  Você é cúmplice, vai ser preso junto ao assassino".ljust(largura - 1) + "|")
elif nivelSuspeito == 5:
    print("|  Você é o assassino, irá ser preso".ljust(largura - 1) + "|")
else:
    print("|  Você é inocente, tá liberado".ljust(largura - 1) + "|")

print("-" * largura)
