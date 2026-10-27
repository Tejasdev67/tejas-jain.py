def run_calculator():
    print("====================================")
    print("      Simple Text Calculator        ")
    print("====================================")

    while True:
        # Get the first number with error handling
        num1_input = input("\nEnter the first number (or type 'exit' to quit): ").strip()
        if num1_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        # Get the second number
        num2_input = input("Enter the second number: ").strip()

        # Validate inputs are numeric (handles floats as well)
        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        # Get the operator
        operator = input("Enter an operator (+, -, *, /): ").strip()

        # Perform logic check based on the operator
        if operator == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operator == '/':
            # Check for division by zero error
            if num2 == 0:
                print("❌ Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("❌ Invalid operator! Please use +, -, *, or /.")

if __name__ == "__main__":
    run_calculator()