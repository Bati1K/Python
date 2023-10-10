# Python Function -----------------------
def greet(name):
    """
    This function takes a name as an argument and prints a greeting message.
    """
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")

# Function Argument----------------------
def add(a, b):
    """
    This function takes two numbers as arguments and returns their sum.
    """
    return a + b

result = add(5, 3)
print("Sum:", result)

# Python Recursion-----------------------
def factorial(n):
    """
    This function calculates the factorial of a number using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

fact = factorial(5)
print("Factorial of 5:", fact)

# Anonymous Function (Lambda)------------
square = lambda x: x * x
print("Square of 4:", square(4))

# Global, Local, and Nonlocal Variables-------------------
x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print("Global variable x:", x)
    print("Local variable y:", y)

my_function()

def outer_function():
    z = 15  # Local variable in the outer function
    
    def inner_function():
        nonlocal z  # Nonlocal variable, modifying the z from outer_function
        z = 20

    inner_function()
    print("Modified nonlocal variable z:", z)

outer_function()

# Python Global Keyword
global_var = 50

def change_global():
    global global_var  # Using the global keyword to modify the global variable
    global_var = 100

change_global()
print("Modified global_var:", global_var)
