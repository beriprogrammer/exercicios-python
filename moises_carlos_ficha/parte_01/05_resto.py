print("CALCULADORA DE RESTO")

numDeOperacao = int(input("Digite o número de operações que deseja fazer: "))

print("========================================")
for i in range(numDeOperacao):

        
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resto = num1 % num2

        print(f"O resto da divisão de {num1} por {num2} é {resto}")
        
        print("-------------------------------------------")

        