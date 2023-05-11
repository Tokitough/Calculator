def calculator():
    try:
        # Ask user to choose an operation
        print("Please choose an operation -\n"
              "1. Addition\n"
              "2. Subtraction\n"
              "3. Multiplication\n"
              "4. Division\n")
        # Get user input for operation
        operation = int(input("Choose one of the four math operations (1-4): "))

        # Get user input for two numbers
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        
        # Perform operation based on user input
        if operation == 1:
            result = num_1 + num_2
        elif operation == 2:
            result = num_1 - num_2
        elif operation == 3:
            result = num_1 * num_2
        elif operation == 4:
            result = num_1 / num_2
        else:

            # If invalid operation number
            print("Invalid operation number.")
            calculator()