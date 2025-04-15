# https://github.com/moritaporretti/lab10-MP-AN.git
# Partner 1: Morita Porretti
# Partner 2: Alula Nahu

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm: base must be > 0 and != 1, and b must be > 0")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


