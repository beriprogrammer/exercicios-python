# 46. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10\. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:  
#     Tabuada de 5:  
#     5 X 1 \= 5  
#     5 X 2 \= 10 
#     ...
#     5 X 10 \= 50


try:
    # 1. Pede ao usuário o número da tabuada
    numero = int(input("Digite um número inteiro entre 1 e 10 para ver a tabuada: "))

    # 2. Verifica se o número está no intervalo válido
    if 1 <= numero <= 10:
        print(f"\nTabuada de {numero}:")
        
        # 3. Usa um loop para calcular e exibir a tabuada
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} X {i} = {resultado}")
    else:
        print("Número inválido! Por favor, digite um número entre 1 e 10.")

except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")