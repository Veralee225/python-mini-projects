# from replit import clear
from art import logo
print(logo)

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

def calculator():
    print(logo)

num1 = float(input("What's the first number?: "))

for s in symbols:
    print(s)
should_continue = True

while should_continue:
    operation_symbols = input("Pick an operation from the line above: ")

num2 = float(input("What's the second number?: "))

calculation_func = symbols[operation_symbols]
answer = calculation_func(num1, num2)

print(f"{num1} {operation_symbols} {num2} = {answer}")

if input(f"Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation: ") == 'y':
    num1 = answer
else:
    should_continue = False
    clear()
    calculator()
