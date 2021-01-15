# task3_160121
"""
Fraction
Create a Fraction class, which will represent all basic arithmetic logic for fractions
(+, -, /, *)with appropriate checking and error handling
class Fraction:
pass
x = Fraction(1/2)
y = Fraction(1/4)
x + y == Fraction(3/4)
"""


def calculate(a, b, action):
    try:
        float(a)
        float(b)
        if action == '+':
            return a+b
        elif action == '-':
            return a-b
        elif action == '*':
            return a*b
        elif action == '/':
            return a/b
        else:
            return 'Wrong action'
    except TypeError:
        return 'Wrong type for operand'
    except ValueError:
        return 'Wrong type for operand'
    except ZeroDivisionError:
        return 'Division by zero'


class Fraction:
    def __init__(self, value: float):
        self.value = value

    def __add__(self, other):
        return calculate(self.value, other.value, '+')

    def __sub__(self, other):
        return calculate(self.value, other.value, '-')

    def __truediv__(self, other):
        return calculate(self.value, other.value, '/')

    def __mul__(self, other):
        return calculate(self.value, other.value, '*')


if __name__ == "__main__":
    x = Fraction(1/2)
    y = Fraction(1/4)
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)


