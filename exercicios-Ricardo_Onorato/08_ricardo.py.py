#8. Verifique se um número inteiro é par.

try:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} não é par")

except ValueError:
    print("por favor, digite um numero inteiro.")




# usando o operador de módulo (%) que retorna o resto de uma divisão.
# um número é par quando o resto da divisão por 2 é igual a zero.