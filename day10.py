#function with outputs

# def my_function():
#     result = 3+2
#     return result
#
# output = my_function()
# print(output)

# def format_names(f_name, l_name):
#     full_name = f_name + ' ' + l_name
#     formatted_name = full_name.title()
#     return formatted_name
#
# output = format_names('mADhav', 'sharma')
# print(output)

# def format_names(f_name, l_name):
#     """Takes first and last name as input and outputs the title case version of the full name"""
#     if f_name == '' or l_name == '':
#         return 'no input'
#     full_name = f_name + ' ' + l_name
#     formatted_name = full_name.title()
#     return formatted_name
#
# output = format_names('', 'sharma')
# print(output)




#Calculator

# def add(n1, n2):
#     sum = n1+n2
#     return sum
#
# def sub(n1, n2):
#     subt = n1 - n2
#     return subt
#
# def multiply(n1, n2):
#     mul = n1*n2
#     return mul
#
# def divide(n1, n2):
#     div = n1/n2
#     return div
#
#
# first_number = int(input("What is the first number? "))
# operation = input("+\n-\n*\n/\n Pick an operation: ")
# second_number = int(input("What is the second number? "))
#
# if operation == '+':
#     print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
#     result = add(first_number, second_number)
# if operation == '-':
#     print(f"{first_number} - {second_number} = {sub(first_number, second_number)}")
#     result = sub(first_number, second_number)
# if operation == '*':
#     print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")
#     result = multiply(first_number, second_number)
# if operation == '/':
#     print(f"{first_number} / {second_number} = {divide(first_number, second_number)}")
#     result = divide(first_number, second_number)
#
# input(f"Type y to continue with {result}, or type n to start a new calculation: ")
# input("+\n-\n*\n/\n Pick an operation: ")
# third_number = int(input("What is the second number? "))



def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    first_number = float(input('What is the first number? '))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation = input("Choose operation: ")
        second_number = float(input("What is the next number? "))
        calculate = operations[operation]
        answer = calculate(first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {answer}")

        if input(f"Type y to continue calculation with {answer} or n to start new calculation:") == 'y':
            first_number = answer
        else:
            should_continue = False
            calculator()

calculator()


