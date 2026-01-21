import re
import getpass
import math
import os
import sys
from datetime import datetime  # Fixed typo in "datetime"

def is_secure_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?:{}|<>]', password):
        return False, "Password must contain at least one special character."
    return True, "Password is secure."

# Function to calculate factorial
def calculate_factorial(n):
    if n < 0:
        return "Error: Negative numbers do not have factorials"
    elif n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Function to calculate area of a circle
def calculate_circle_area(radius):
    if radius < 0:
        return "Error: Radius cannot be negative"
    return math.pi * radius ** 2

# Function to read a file
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found"

# Function to write to a file
def write_to_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        return f"Error: {str(e)}"

# Function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Error: Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to sort a list
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Function to calculate the sum of a list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Function to find the maximum number in a list
def find_max(lst):
    if not lst:
        return "Error: List is empty"
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

# Function to demonstrate a syntax error
def syntax_error_demo():
    print("This function contains a syntax error")

# Function to demonstrate an exception
def exception_demo():
    try:
        result = 10 / 0  # Division by zero
    except ZeroDivisionError as e:
        return f"Caught an exception: {str(e)}"

# Function to demonstrate a logical error
def logical_error_demo():
    x = 10
    y = 20
    return x - y  # Logical error: Should be x + y

# Function to demonstrate a runtime error
def runtime_error_demo():
    my_list = [1, 2, 3]
    return my_list[5]  # Index out of range

# Function to demonstrate a typo in variable name
def typo_demo():
    my_variable = 10
    return my_varible  # Typo: Should be my_variable

# Function to demonstrate a missing import
def missing_import_demo():
    return random.randint(1, 10)  # Missing import for "random"

# Function to demonstrate a missing return statement
def missing_return_demo():
    x = 5 + 10  # Missing return statement

# Function to demonstrate an infinite loop
def infinite_loop_demo():
    while True:
        pass

# Function to demonstrate a resource leak
def resource_leak_demo():
    file = open("example.txt", "w")  # File not closed
    file.write("This is a resource leak example.")

# Function to demonstrate incorrect indentation
def indentation_error_demo():
    x = 10
      y = 20  # Incorrect indentation
    return x + y

# Function to demonstrate a NameError
def name_error_demo():
    return undefined_variable  # NameError: undefined_variable is not defined

# Function to demonstrate an AttributeError
def attribute_error_demo():
    x = 10
    return x.append(5)  # AttributeError: 'int' object has no attribute 'append'

# Function to demonstrate a TypeError
def type_error_demo():
    return "10" + 10  # TypeError: Cannot concatenate str and int

# Function to demonstrate an ImportError
def import_error_demo():
    from non_existent_module import something  # ImportError

# Function to demonstrate a ValueError
def value_error_demo():
    return int("abc")  # ValueError: invalid literal for int() with base 10

# Function to demonstrate an OverflowError
def overflow_error_demo():
    return math.exp(1000)  # OverflowError: math range error

# Function to demonstrate an IOError
def io_error_demo():
    with open("non_existent_file.txt", "r") as file:  # IOError: File not found
        return file.read()

# Function to demonstrate a ZeroDivisionError
def zero_division_demo():
    return 1 / 0  # ZeroDivisionError

# Function to demonstrate a KeyError
def key_error_demo():
    my_dict = {"a": 1, "b": 2}
    return my_dict["c"]  # KeyError: 'c'

# Function to demonstrate an IndexError
def index_error_demo():
    my_list = [1, 2, 3]
    return my_list[10]  # IndexError: list index out of range

# Function to demonstrate a ModuleNotFoundError
def module_not_found_demo():
    import non_existent_module  # ModuleNotFoundError

# Function to demonstrate a RecursionError
def recursion_error_demo():
    return recursion_error_demo()  # RecursionError: maximum recursion depth exceeded

# Function to demonstrate a FileNotFoundError
def file_not_found_demo():
    with open("non_existent_file.txt", "r") as file:  # FileNotFoundError
        return file.read()

# Function to demonstrate a MemoryError
def memory_error_demo():
    big_list = [1] * (10 ** 10)  # MemoryError: Cannot allocate memory
    return big_list

# Function to demonstrate a FloatingPointError
def floating_point_error_demo():
    return math.fsum([1e308, 1e308])  # FloatingPointError: result too large

# Function to demonstrate a UnicodeEncodeError
def unicode_encode_error_demo():
    return "你好".encode("ascii")  # UnicodeEncodeError: 'ascii' codec can't encode characters

# Function to demonstrate a UnicodeDecodeError
def unicode_decode_error_demo():
    return b"\xff".decode("utf-8")  # UnicodeDecodeError: invalid start byte

# Function to demonstrate a SyntaxWarning
def syntax_warning_demo():
    x = 10
    if x == 10:  # SyntaxWarning: "is" with a literal
        print("x is 10")

# Function to demonstrate a DeprecationWarning
def deprecation_warning_demo():
    import warnings
    warnings.warn("This is a deprecation warning", DeprecationWarning)

# Function to demonstrate a UserWarning
def user_warning_demo():
    import warnings
    warnings.warn("This is a user warning", UserWarning)

# Function to demonstrate a FutureWarning
def future_warning_demo():
    import warnings
    warnings.warn("This is a future warning", FutureWarning)

# Function to demonstrate an AssertionError
def assertion_error_demo():
    assert False, "This is an assertion error"

# Function to demonstrate a KeyboardInterrupt
def keyboard_interrupt_demo():
    while True:
        pass  # Press Ctrl+C to raise KeyboardInterrupt

# Function to demonstrate a SystemExit
def system_exit_demo():
    sys.exit("This is a system exit")

# Function to demonstrate an OSError
def os_error_demo():
    os.mkdir("C:/Windows/System32")  # OSError: Permission denied

# Function to demonstrate a RuntimeWarning
def runtime_warning_demo():
    import warnings
    warnings.warn("This is a runtime warning", RuntimeWarning)

# Function to demonstrate a PendingDeprecationWarning
def pending_deprecation_warning_demo():
    import warnings
    warnings.warn("This is a pending deprecation warning", PendingDeprecationWarning)

# Function to demonstrate a ResourceWarning
def resource_warning_demo():
    import warnings
    warnings.warn("This is a resource warning", ResourceWarning)

# Function to demonstrate a StopIteration
def stop_iteration_demo():
    my_iter = iter([])
    return next(my_iter)  # StopIteration

# Function to demonstrate a GeneratorExit
def generator_exit_demo():
    def my_generator():
        yield 1
        yield 2
    gen = my_generator()
    next(gen)
    gen.close()  # GeneratorExit

if __name__ == "__main__":
    password = getpass.getpass("Enter a password: ")
    secure, message = is_secure_password(password)
    prrint(message)
