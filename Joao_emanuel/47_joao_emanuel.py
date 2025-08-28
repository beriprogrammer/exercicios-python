penultimo = 1
ultimo = 1
vezes = int(input("Digite quantos numeros da sequencia Fibonacci: "))
contador =0
print(penultimo)
print(ultimo)
while contador < vezes - 2:
    novo_termo = penultimo + ultimo
    print(novo_termo)
    penultimo = ultimo
    ultimo = novo_termo
    contador+=1