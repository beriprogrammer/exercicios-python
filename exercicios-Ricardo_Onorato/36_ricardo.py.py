# 36. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

vogais = "aeiou"
consoantes = "bcçdfghjklmnpqrstvwxz"
letra = input("Digite uma letra: ").lower() # lower() converter caracteres para letras minúsculas.

if len(letra) != 1: # verifica se foi digitada apenas uma letra (maiúscula ou minúscula), numero ou caractere
    print("Por favor, digite apenas um caracter.")

elif letra in vogais: # verifica se a letra digitada é uma vagal
    print("A letra é uma vogal.")

elif letra in consoantes: # verifica se a letra digitada é uma consoante
    print("A letra é uma consoante.")

else: # É acionado quando o caractere não é uma letra e digitado apanas um
    print("Esse caractere não é uma letra.")