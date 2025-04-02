from colorama import *

# This is a simple calculator program that performs basic arithmetic operations
# such as addition, subtraction, multiplication, and division.
# It takes two numbers and an operator as input from the user and returns the result.

# The program uses the colorama library to add color to the output.
# The user is prompted to enter two numbers and an operator.
# The program then performs the operation and prints the result in a colored format.
# The program also handles division by zero and invalid operator inputs.
# The program continues to run until the user chooses to exit.

# Addition.
def add(x, y):
    return x + y
# Subtraction.
def subtract(x, y):
    return x - y
# Multiplication.
def multiply(x, y):
    return x * y
# Division.
def divide(x, y):
    if y == 0:
        print(Fore.RED + "Error: Division by Zero is not allowed." + Style.RESET_ALL)
        return None
    else:
        return x / y

# Function to display the menu and get user input.
print(Fore.CYAN + "[!] - Welcome to the Simple Calculator!" + Style.RESET_ALL)
print(Fore.YELLOW + "[*] - Please select an operation:" + Style.RESET_ALL)
print(Fore.GREEN + "[1] - Addition" + Style.RESET_ALL)
print(Fore.GREEN + "[2] - Subtraction" + Style.RESET_ALL)
print(Fore.GREEN + "[3] - Multiplication" + Style.RESET_ALL)
print(Fore.GREEN + "[4] - Division" + Style.RESET_ALL)
print(Fore.RED + "[5] - Exit" + Style.RESET_ALL)    

# Get user input for operation choice.
input_choice = input(Fore.YELLOW + "[#] - Enter your choice (1-5):" + Style.RESET_ALL)
# Check if the input is a valid number.
if input_choice.isdigit():
    choice = int(input_choice)
else:
    print(Fore.RED + "[!] - Invalid input. Please enter a number between 1 and 5." + Style.RESET_ALL)
    exit()

# Check if the choice is valid.
if choice < 1 or choice > 5:
    print(Fore.RED + "[!] - Invalid choice. Please select a number between 1 and 5." + Style.RESET_ALL)
    exit()

# If the user chooses to exit, print a goodbye message and exit.
if choice == 5:
    print(Fore.CYAN + "[!] - Thank you for using the Simple Calculator. Goodbye!" + Style.RESET_ALL)
    exit()

# Get user input for numbers.
num1 = input(Fore.YELLOW + "[x] - Enter the first number:" + Style.RESET_ALL)
num2 = input(Fore.YELLOW + "[x] - Enter the second number:" + Style.RESET_ALL)

# Check if the inputs are valid numbers.
if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
    print(Fore.RED + "[!] - Invalid input. Please enter valid numbers." + Style.RESET_ALL)
    exit()

# Convert the inputs to floats.
num1 = float(num1)
num2 = float(num2)

# Perform the operation based on user choice.
if choice == 1:
    result = add(num1, num2)
    print(Fore.GREEN + "[+] - The result of addition is: " + str(result) + Style.RESET_ALL)
elif choice == 2:
    result = subtract(num1, num2)
    print(Fore.GREEN + "[-] - The result of subtraction is: " + str(result) + Style.RESET_ALL)
elif choice == 3:
    result = multiply(num1, num2)
    print(Fore.GREEN + "[*] - The result of multiplication is: " + str(result) + Style.RESET_ALL)
elif choice == 4:
    result = divide(num1, num2)
    if result is not None:
        print(Fore.GREEN + "[/] - The result of division is: " + str(result) + Style.RESET_ALL)

# Print a goodbye message.
print(Fore.CYAN + "[!] - Thank you for using the Simple Calculator. Goodbye!" + Style.RESET_ALL)

# End of the calculator program.

# We have more features we have in mind like adding more features such as:
# - Support for more complex operations (e.g., exponentiation, square root).
# - Support for parentheses and operator precedence.
# - A graphical user interface (GUI) for better user experience.
# - Error handling for invalid inputs and operations.
# - A history feature to keep track of previous calculations.
# - A scientific calculator mode for advanced calculations.
# - A memory feature to store and recall previous results.
# - A unit converter for converting between different units of measurement.
# - A currency converter for converting between different currencies.
# - A percentage calculator for calculating percentages.
# - A loan calculator for calculating monthly payments and interest rates.
# - A BMI calculator for calculating body mass index.
# - A tip calculator for calculating tips and total amounts.
# - A date calculator for calculating differences between dates.