numero = int(input("Digite um numero para a tabuada: "))
print(f"A tabuada de {numero} é: ")
print("-"*12)
for contador in range(1,11):
    print(f"{numero} x {contador} = {numero*contador}")
print("-"*12)
