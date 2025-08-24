print("\n* Check if an integer is within a specific range *\n")

startRange = int(input("Type the start  of the range: "))

endRange = int(input("type the end of  the range: "))

number = int(input("Type a number: "))

if startRange >= number <= endRange:
    print(f"The {number} is within")
else:
    print("Diferent")
