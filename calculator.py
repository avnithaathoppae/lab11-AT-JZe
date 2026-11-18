"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): 
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a 
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def logarithm(a, b): 
    try:
        return math.log(b, a)
    except ValueError:
        print("Error: Invalid input for logarithm.")
        return None

def exponent(a, b):
    return a ** b

