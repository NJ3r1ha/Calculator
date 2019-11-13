while True:
    print("""
    Please choose math operation you would like to complete:
    + Addition
    - Subtraction
    * Multiplication
    / Division
    """)

    math_operation = input("Enter your choice (+, -, *, /): ")

    number_1 = input("Enter first number: ")
    number_2 = input("Enter second number: ")

    try:
        if math_operation == "+":
            answer = float(number_1) + float(number_2)
        elif math_operation == "-":
            answer = float(number_1) - float(number_2)
        elif math_operation == "*":
            answer = float(number_1) * float(number_2)
        elif math_operation == "/":
            answer = float(number_1) / float(number_2)
    except ValueError:
        print("Please provide integer or float number.")
    else:
        print(answer)

    calc_again = input("Would you like to calculate again? Enter 'y' or 'n': ")
    if calc_again.lower() == "y":
        continue
    elif calc_again.lower() == "n":
        print("See you later.")
        break
    else:
        print("You didn't choose right letter.")
        break
