'''num1 = int(input("Digite o valor do dividendo: "))
num2 = int(input("Digite o valor do divisor: "))

resto = num1 % num2

if resto == 0:
    print(f"O numero {num1} e divisivel por {num2}.")

else:
    print(f"O numero {num1} nao e divisivel por {num2}.") '''

num1 = int(input("Digite o valor do dividendo: "))
num2 = int(input("Digite o valor do divisor: "))

resto = num1 % num2

print(f"O numero {num1} e divisivel por {num2}? {resto == 0 }")