# 12. Verifique se dois números inteiros são diferentes.

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if numero1 != numero2:
        print(f"Os números informados são diferentes")
    else:
        print(f"Os números informados são iguais")

except ValueError:
    print("por favor, digitar apenas números inteiros.")