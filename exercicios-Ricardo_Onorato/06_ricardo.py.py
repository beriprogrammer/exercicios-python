#6. Verifique se um número inteiro é positivo.

try:
   numero = int(input("Digite o número inteiro: "))

   if numero > 0:
      print(f"{numero} é um número inteiro positivo.")

   elif numero < 0:
      print(f"{numero} não é um número inteiro positivo, ele é um numero negativo.")

except ValueError:
   print(f"Por favor, digite um número inteiro")

# uso do bloco try-except para garantir que o programa não pare de funcionar caso o usuário digite algo que não seja um número.