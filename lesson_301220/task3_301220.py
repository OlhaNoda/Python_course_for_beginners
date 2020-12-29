# task3_301220
"""
Task 3
A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator
as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter.
For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""


def make_operations(operator, first_number, *args):
    return_value = first_number
    if operator in ('+', '-', '*'):
        for number in args:
            if operator == '+':
                return_value += number
            elif operator == '-':
                return_value -= number
            else:
                return_value *= number
        print(return_value)
    else:
        print('The operator is wrong')


make_operations('-', 6, 1, 3)
