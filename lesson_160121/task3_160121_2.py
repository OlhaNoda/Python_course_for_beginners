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


class Fraction:
    def __init__(self, value: float):
        self.value = value

    def __add__(self, other):
        try:
            float(self.value)
            float(other.value)
            return self.value + other.value
        except ValueError:
            return 'Wrong type for operand'

    def __sub__(self, other):
        try:
            return self.value - other.value
        except TypeError:
            return 'Wrong type for operand'

    def __mul__(self, other):
        try:
            float(self.value)
            float(other.value)
            return self.value * other.value
        except ValueError:
            return 'Wrong type for operand'

    def __truediv__(self, other):
        try:
            return self.value / other.value
        except TypeError:
            return 'Wrong type for operand'
        except ZeroDivisionError:
            return 'Division by zero'


if __name__ == "__main__":
    x = Fraction(1/2)
    y = Fraction(1/4)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
