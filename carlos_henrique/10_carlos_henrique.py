print("\n* Check if a number is divisible by another number *\n")

dividend = int(input("Enter the dividend: "))

divisor = int(input("Enter the divisor: "))

if dividend % divisor == 0:
    print(f"{dividend} is divisible by {divisor}.")
else:
    print(f"{dividend} is not divisible by {divisor}.")
