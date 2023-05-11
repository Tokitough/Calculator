def calculator():
    try:
        # Ask user to choose an operation
        print("=" * 45)
        print("Please choose an operation: \n"
              "1. Addition\n"
              "2. Subtraction\n"
              "3. Multiplication\n"
              "4. Division")
        print("=" * 45)
        
        # Get user input for operation
        operation = int(input("Choose one of the four math operations (1-4): "))

        # Get user input for two numbers
        print("=" * 45)
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
        print("=" * 45)
        
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

        # Display the result
        print("The result is:", result)

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (y/n): ")

        if another_calculation.lower() == 'y':
            calculator()
        else:
            # End if user does not want to perform another calculation
            print("Thank you for using the simple calculator app")
            
    # Handle runtime errors
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero.")
        calculator()
    except ValueError:
        # Handle invalid input error
        print("=" * 45)
        print("Error: Invalid input.")
        calculator()

calculator()