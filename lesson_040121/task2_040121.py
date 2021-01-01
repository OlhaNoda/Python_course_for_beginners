# task1_040121
"""
Task 2
Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block
which raises an exception if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero).
"""


def squared_a_divided_by_b(a, b):
    return a ** 2 / b


if __name__ == "__main__":
    print("Let's calculate a**2/b !")
    while True:
        try:
            print(f"a**2/b= {squared_a_divided_by_b(int(input('Enter a number а: ')), int(input('Enter a nonzero number b : ')))}")
            break
        except ValueError:
            print('That was no valid number. Try it again!')
        except ZeroDivisionError:
            print('Division by zero. You have to enter a nonzero number b. Try it again!')
