def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    while True:
        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an operation: ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))

calculator()



# Simple Calculator
 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
    print("Result:", result)
 
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
 
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
 
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero")
 
else:
    print("Invalid operation")