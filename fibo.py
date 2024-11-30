from colorama import Fore, Style, init

# Initialize colorama (important for Windows)
init(autoreset=True)

# Function to return the nth Fibonacci number using recursion
def fibonacci(n):
    # Base case: return 0 if n is 0, return 1 if n is 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function to print the Fibonacci series with color styles
def fibonacci_series(n):
    for i in range(n):
        fib_num = fibonacci(i)
        # Assign a color for each Fibonacci number
        if fib_num % 2 == 0:
            print(Fore.GREEN + str(fib_num), end=" ")  # Green for even numbers
        else:
            print(Fore.RED + str(fib_num), end=" ")  # Red for odd numbers

# Take input from the user for the number of terms in the Fibonacci series
try:
    n = int(input("Enter the number of terms for the Fibonacci series: "))
    if n < 0:
        print(Fore.YELLOW + "Please enter a positive integer.")
    else:
        print(f"{Style.BRIGHT}{Fore.CYAN}Fibonacci series up to {n} terms:")
        fibonacci_series(n)
except ValueError:
    print(Fore.YELLOW + "Invalid input. Please enter an integer.")
