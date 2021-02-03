# task1_030221
"""
Imports practice
Make a directory with 2 modules; make a function in one of them;
then import this function in the other module and use that in your script of choice.
"""


def add(*args):
    s = 0
    for number in args:
        s = s + number
    return s


def power_to(power, *args):
    return [number ** power for number in args]
