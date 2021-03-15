import time
from concurrent.futures import ProcessPoolExecutor


def get_fibonacci(number: int) -> int:
    index = number - 2
    fib1 = fib2 = 1
    while index > 0:
        fib1, fib2 = fib2, fib1 + fib2
        index -= 1
    return fib2


def get_factorial(number: int) -> int:
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


def get_square(number: int) -> int:
    return number**2


def get_cubic(number: int) -> int:
    return number**3


def process_execution(amount: int):
    start = time.time()
    with ProcessPoolExecutor() as executor:
        fibonacci = list(executor.map(get_fibonacci, range(1, amount+1)))
        factorial = list(executor.map(get_factorial, range(1, amount+1)))
        square = list(executor.map(get_square, range(1, amount+1)))
        cubic = list(executor.map(get_cubic, range(1, amount+1)))

    print('Start process_execution: {} Time taken: {}'.format(start, time.time()-start))
    return fibonacci, factorial, square, cubic


if __name__ == '__main__':
    print(process_execution(10))
