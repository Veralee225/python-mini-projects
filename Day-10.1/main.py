from art import logo
#from replit import clear

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

dict = {}

symbols = {
    "+": add,
    "-": substract,
    "/": divide,
    "*": multiply
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for s in symbols:
    print(s)
operation_symbols = input("Pick an operation from the line above: ")

calculation_func = symbols[operation_symbols]
answer = calculation_func(num1, num2)
