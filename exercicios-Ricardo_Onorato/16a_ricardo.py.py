#16. Realize uma operação lógica "OU" entre dois booleanos.

# sistema para aquecimento de metais
botaoA = True
botaoB = True
botaoC = True
botaoD = False
botaoE = True
botaoF = True
botaoG = True

if botaoA: # acionar o botão para ligar/desligar
    print("ligado")
    if botaoB: # liga apra aquecer.o botão A também tem que estar acionado
        print("aquecer ")
        if botaoC or botaoD: # liga para derreter. os botões A e B também tem que estar acionados o C aciona 40% do derretimento, o D 60%, os 2 100%
            print("derreter")
    elif botaoE:  # liga para desaquecer.o botão A também tem que estar acionado
        print("Desaquecer.")
        if botaoF or botaoG: # liga para derreter. os botões A e B também tem que estar acionados o F aciona 40% do resfriamento, o G 60%, os 2 100%
            print("Resfriar.")
else:
    print("desligado") # se o botão A não for acionado ou, quando ligado, acionado para desligamento.

# obs para a parte de resfriamento(botãoE) funcionar, tem que acionar esse botãoE(true) e desabilitar o (botãoB) de aquecimento. ou seja, desligar(false)
# obs2 a parte de operação lógica com "OU" entre dois booleanos foram realizadas nas linha 16 e 20.  
