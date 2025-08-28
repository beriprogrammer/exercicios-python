#11. Verifique se dois números inteiros são iguais.

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if numero1 == numero2:
        print(f"Os números informados são iguais")
    else:
        print(f"Os números informados são diferentes")

except ValueError:
    print("por favor, digitar apenas números inteiros.")