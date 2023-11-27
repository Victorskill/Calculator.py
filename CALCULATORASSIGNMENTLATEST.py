import os

def add(x, y):
    return int(x + y) if (x + y).is_integer() else x + y

def subtract(x, y):
    return int(x - y) if (x - y).is_integer() else x - y

def multiply(x, y):
    return int(x * y) if (x * y).is_integer() else x * y

def divide(x, y):
    if y != 0:
        result = x / y
        return int(result) if result.is_integer() else result
    else:
        return "Cannot divide by zero!"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message
print("Welcome to the Calculator App!")

while True:
    # Display options
    print("\nOptions:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get user choice
    choice = input("Enter the number of your choice (1-5): ")

    if choice not in {'1', '2', '3', '4', '5'}:
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    if choice == '5':
        print("Thank you for using our calculator!")
        break

    try:
        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    # Perform the chosen operation and display the result
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    print(f"Result: {result}")

    # Ask if the user wants to do another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()

    if another_calculation != 'yes':
        print("Thank you for using our app!")
        break
    else:
        clear_console()  # Clear the console for a new calculation
