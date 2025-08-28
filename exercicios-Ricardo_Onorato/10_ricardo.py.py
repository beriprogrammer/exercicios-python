# 10. Verifique se um número inteiro é divisível por outro.

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if numero2 == 0:
        print(f"Atenção! o segundo número não pode ser {numero2} (zero).")
    elif numero1 % numero2 == 0 and numero2 != 0:
        print(f"O número {numero1} é divisível pelo número {numero2}")
    
    else:
        print(f"O número {numero1} não é divisível pelo número {numero2}")

except ValueError:
    print("Por favor, digite um número inteiro.")
    