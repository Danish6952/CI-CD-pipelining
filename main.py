print("Simple Calculator")


a1 = float(input("Enter your first number: "))
b1 = float(input("Enter your second number: "))

print("Choose an operation:")
print("1. Multiply (*)")
print("2. Add (+)")
print("3. Subtract (-)")


i = input("Enter the number of the operation: ")

if i == "1":
    print("Result:", a1 * b1)
elif i == "2":
    print("Result:", a1 + b1)
elif i == "3":
    print("Result:", a1 - b1)
else:
    print("Wrong Input")
