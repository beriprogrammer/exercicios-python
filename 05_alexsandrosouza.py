#5- Calcule o resto da divisão entre dois números inteiros.

def verificaResto():
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o número divisor: "))


    if dividendo != 0:
        resto = dividendo % divisor
        print(f"O resto da divisão de {dividendo} por {divisor} é {resto}.")
    else:
        print("Erro: divisão por zero não é permitida.")

verificaResto()