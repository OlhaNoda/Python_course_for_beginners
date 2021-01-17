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

import math


def reduce_fraction(a: int, b: int):
    greatest_common_divisor = math.gcd(a, b)
    a = int(a / greatest_common_divisor)
    b = int(b / greatest_common_divisor)
    return a, b


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError('Wrong type. The numbers must be integer')
        if denominator == 0:
            raise ZeroDivisionError('The denominator cannot be zero')
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        numerator = int((self.numerator * other.denominator) + (other.numerator * self.denominator))
        denominator = int(self.denominator * other.denominator)
        numerator, denominator = reduce_fraction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = int((self.numerator * other.denominator) - (other.numerator * self.denominator))
        denominator = int(self.denominator * other.denominator)
        numerator, denominator = reduce_fraction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = int(self.numerator * other.numerator)
        denominator = int(self.denominator * other.denominator)
        numerator, denominator = reduce_fraction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = int(self.numerator * other.denominator)
        denominator = int(self.denominator * other.numerator)
        numerator, denominator = reduce_fraction(numerator, denominator)
        return Fraction(numerator, denominator)

    def __str__(self):
        if self.denominator == 1:
            return f'{self.numerator}'
        elif self.numerator < self.denominator:
            return f'{self.numerator}/{self.denominator}'
        else:
            return f'{self.numerator//self.denominator} {self.numerator%self.denominator}/{self.denominator}'


if __name__ == "__main__":
    x = Fraction(5, 1)
    y = Fraction(1, 2)
    print(f'{x} + {y} = {x + y}')
    print(f'{x} - {y} = {x - y}')
    print(f'{x} * {y} = {x * y}')
    print(f'{x} : {y} = {x / y}')
