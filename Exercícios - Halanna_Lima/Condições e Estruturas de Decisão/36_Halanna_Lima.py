#Verificar se uma letra digitada é vogal ou consoante.

letra = str(input("Oi divo(A)digite uma letra: "))

if letra.isupper():
    print("Oia, uma letra Maiuscula")
elif letra.islower() :
    print("Uia uma letra minuscula")
else :
    print("Isso não é uma letra")
