def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    operation = input("Choose the operation (+, -, *, /): ").strip()

    if operation == "+":
        result = num1 + num2
        print(f"The result is {result}.")
    elif operation == "-":
        result = num1 - num2
        print(f"The result is {result}.")
    elif operation == "*":
        result = num1 * num2
        print(f"The result is {result}.")
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    else:
        print("Invalid operation. Please choose from +, -, *, /.")

if __name__ == "__main__":
    main()
