
start = int(input("\nEnter the lower limit: "))
stop = int(input("Enter the upper limit: "))
number = int(input("Enter a number: "))

# Conditional to check if the number is within the interval
if start <= number <= stop:
    print("\nNumber within the interval.")
    print(f"{start}",5*".",f"*{number}*",5*".",f"{stop}")

else:
    print("\nThis number is not in the interval")
    print(f"{start}", 5 * ".", f"!X!", 5 * ".", f"{stop}")

