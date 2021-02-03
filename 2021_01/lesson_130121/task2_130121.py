# task2_130121
"""
Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""


class Mathematician:
    def __init__(self, list_of_integers):
        self.list_of_integers = list_of_integers

    def square_nums(self):
        return [i**2 for i in self.list_of_integers]

    def remove_positives(self):
        return [i for i in self.list_of_integers if i < 0]

    def filter_leaps(self):
        return [i for i in self.list_of_integers if i > 0 and i % 4 == 0]


if __name__ == "__main__":
    m1 = Mathematician([7, 11, 5, 4])
    m2 = Mathematician([26, -11, -8, 13, -90])
    m3 = Mathematician([2001, 1884, 1995, 2003, 2020])
    print(m1.square_nums())
    print(m2.remove_positives())
    print(m3.filter_leaps())
    assert m1.square_nums() == [49, 121, 25, 16], 'Not found'
    assert m2.remove_positives() == [-11, -8, -90], 'Not found'
    assert m3.filter_leaps() == [1884, 2020], 'Not found'

