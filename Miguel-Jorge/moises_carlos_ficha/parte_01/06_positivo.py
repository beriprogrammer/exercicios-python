print("VERIFICADOR DE NÚMEROS POSITIVOS")

numDeOperacao = int(input("Quantos números deseja verificar: "))

print("========================================")
for i in range(numDeOperacao):

        num = int(input("Digite um número: "))
        if num > 0:
            print(f"{num} é um número positivo.")
        else:
            print(f"{num} não é um número positivo.")

        print("-------------------------------------------")
