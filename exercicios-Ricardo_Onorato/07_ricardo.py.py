#7. Verifique se um número inteiro é negativo.

try:
    numero = int(input("Digite um numero inteiro: "))

    if numero < 0:
       print(f"{numero} é um número negativo.")
    elif numero > 0:
        print(f"{numero} não é um número inteiro negativo, ele é um numero positivo.")

except ValueError:
    print("Por favor, digite um número inteiro")  
      
# uso do bloco try-except para garantir que o programa não pare de funcionar caso o usuário digite algo que não seja um número.