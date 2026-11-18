"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def add(a, b):
    return a + b


def mul(a, b):
    return a * b

# raise ZeroDivisionError if a == 0
def div(a, b):
    if a = 0:
        raise ZeroDivisionError("Error. Cannot divide by zero")
    return b / a

# use math library + raise ValueError

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Input must be a non-negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)



def subtract(a, b):
    return a - b





def logarithm(a, b): 
    if b<=0 or a<=0 or a==1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)


