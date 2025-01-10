def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

def subtract(x, y):
    return x - y

subtract_lambda = lambda x, y: x - y

def multiply(x, y):
    return x * y

multiply_lambda = lambda x, y: x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

divide_lambda = lambda x, y: x / y if y != 0 else "Cannot divide by zero"

a, b = 10, 5

print("Addition Function:", add(a, b))
print("Addition Lambda Function:", add_lambda(a, b))

print("Subtraction Function:", subtract(a, b))
print("Subtraction Lambda Function:", subtract_lambda(a, b))

print("Multiplication Function:", multiply(a, b))
print("Multiplication Lambda Function:", multiply_lambda(a, b))

print("Division Function:", divide(a, b))
print("Division Lambda Function:", divide_lambda(a, b))