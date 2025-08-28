# sistema de montagem de veículos
botaoA = True
botaoB = False
botaoC = False
botaoD = False
botaoE = True
botaoF = False
botaoG = False
botaoH = False
botaoI = False
botaoJ = False

if botaoA:
    print("ligado")
    if botaoB:
        print("posiciona o motor ")
        if botaoC or botaoD:
            print("posiciona os pneus")
    elif botaoE:
        print("coloca parabrisas")
        if botaoF or botaoG:
            print("posiciona as poutas")
    elif botaoH:
        print("coloca volante")
        if botaoI or botaoJ:
            print("posiciona os retrovisores")
else:
    print("desligado")