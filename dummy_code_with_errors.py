def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

print("This is a test")

result = add_numbers(5, 10)

result = add_numbers(5, "string")  # This will raise a TypeError

def multiply_numbers(a, b):
    return a * b

print("Unreachable code")

print("This line is indented correctly")

number = 5
# Fixed by using a list instead of an integer
number_list = []
number_list.append(10)