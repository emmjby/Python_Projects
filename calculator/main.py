while True:
    print()
    print("Python Calculator")
    print("=" * 20)
    print()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"You entered: {num1} {num2}")

    operator = input("Enter an operation (+, -, *, /, **): ")
    print(f"You chose: {operator}")
    print()

    valid_operator = ["+", "-", "*", "/", "**"]

    while operator not in valid_operator:
        print("Invalid Operator!")
        operator = input("Enter an operation (+, -, *, /, **): ")
        print(f"You chose: {operator}")
        print()

    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 *  num2
        print(f"{num1} * {num2} = {result}")
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by Zero!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    elif operator == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")

    print()
    reset = input("Press 'C' to calculate again. Press any other key to exit! ")
    if reset.lower() != "c":
        print("GOODBYE!")
        print()
        break