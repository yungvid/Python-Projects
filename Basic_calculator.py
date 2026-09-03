print("----- Basic Calculator -----")
print("----- Calculate Basic Arithmetic Operations -----")
print("----- Type 'exit' to quit the calculator -----")

while True:
    try:
        num1 = input("Enter your first number or type 'exit' to quit: ")
        if num1.lower() == "exit":
            print("Goodbye!")
            break
        num1 = float(num1)

        num2 = input("Enter your second number or type 'exit' to quit: ")
        if num2.lower() == "exit":
            print("Goodbye!")
            break
        num2 = float(num2)

        operation = input("Enter Math Operation (+, -, *, /) or type 'exit' to quit: ")
        if operation.lower() == "exit":
            print("Goodbye!")
            break

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
            continue

        print(f"The result of {num1} {operation} {num2} = {result}") 
        print("-" * 30)

    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")
        print("-" * 30)       




