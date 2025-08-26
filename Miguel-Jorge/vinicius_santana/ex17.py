num1 = int(input("informe um numero: "))

num2 = num1 %2 == 0
num3 = num1 %3 == 0


if num2 ^ num3:
    print(True)
else:
    print(False)