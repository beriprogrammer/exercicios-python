# 9. Verifique se um número inteiro é ímpar.

try:
    numero = int(input("Digite um número: "))

    if numero % 2 != 0:
        print(f"O número {numero} não é par")
    else:
        print(f"O número {numero} é par")

except ValueError:
    print("por favor, digite um numero inteiro.")

# usando o operador de módulo (%) que calcula o resto da divisão do numero por 2. Se o resto da  divisão por 2 for diferente de zero, número é ímpar.