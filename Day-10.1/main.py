from art import logo
from replit import clear

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

dict = {}

sysmbols = {
    "+": add,
    "-": substract,
    "/": divide,
    "*": multiply
}
