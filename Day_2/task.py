# data type

# Subcripting - accessing a specific character in a string
print("Hello"[0]) #prints H

# we can also use negeative numbers to access the last character of a string
print("Hello"[-1]) #prints o

# integer data type - whole numbers

print(123 + 345) #addition

# large integers
print(123_456_789) #prints 123456789

# float data type - decimal numbers - floating point numbers
3.14159

# boolean data type - True or False

# data type and functions

# type() function - returns the data type of a value
print(type("Hello")) #prints <class 'str'>
print(type(123))
print(type(True))
print(type(3.14159))

# type conversion
print(int("123") + int("456"))

#value error - when you try to convert a string that is not a number to an integer
# example of such - int("abc")
int()
float()
str()
bool()

# checking the length of a string
# print("Number of letters in your name: " + len(input("Enter your name")))

user_name = input("Enter your name")

name_length = len(user_name)

print("Number of letters in your name: " + str(name_length))
