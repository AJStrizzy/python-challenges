# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operator = input('What calculation would you like to do? (add, sub, mult, div) ')
num1 = input('What is your first number? ')
num2 = input('What is your second number? ')

def calculator(operator, num1, num2):
    if operator == "add":
        return int(num1) + int(num2)
    elif operator == "sub":
        return int(num1) - int(num2)
    elif operator == "mult":
        return int(num1) * int(num2)
    elif operator == "div":
        return int(num1) / int(num2)           


print(calculator(operator, num1, num2))