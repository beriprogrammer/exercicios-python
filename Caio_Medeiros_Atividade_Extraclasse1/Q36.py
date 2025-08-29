letra = str(input("Digite uma letra: "))

if letra.isalpha():
    if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U":
        print("Vogal")

    else:
        print("Consoante")

else:
    print("Comando digitado não é uma letra.")