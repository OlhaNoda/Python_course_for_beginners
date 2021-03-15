# task1_150321
"""
Practice asynchronous code
Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10.
You need to get four lists of results from corresponding functions.
Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
Time the execution of both realizations, explore the results, what realization is more effective,
why did you get a result like this.
"""
import asyncio
import time


async def get_fibonacci(number: int) -> int:
    index = number - 2
    fib1 = fib2 = 1
    while index > 0:
        # await asyncio.sleep(1)
        fib1, fib2 = fib2, fib1 + fib2
        index -= 1
    return fib2


async def get_factorial(number: int) -> int:
    factorial = 1
    while number > 1:
        # await asyncio.sleep(1)
        factorial *= number
        number -= 1
    return factorial


async def get_square(number: int) -> int:
    # await asyncio.sleep(1)
    return number**2


async def get_cubic(number: int) -> int:
    # await asyncio.sleep(1)
    return number**3


def gather_tasks(amount: int):
    start = time.time()

    loop = asyncio.get_event_loop()

    fibonacci = asyncio.gather(*[get_fibonacci(i) for i in range(1, amount+1)])
    factorial = asyncio.gather(*[get_factorial(i) for i in range(1, amount+1)])
    square = asyncio.gather(*[get_square(i) for i in range(1, amount+1)])
    cubic = asyncio.gather(*[get_cubic(i) for i in range(1, amount+1)])

    all_tasks = asyncio.gather(fibonacci, factorial, square, cubic)
    results = loop.run_until_complete(all_tasks)

    loop.close()

    print('Start asyncio_execution: {} Time taken: {}'.format(start, time.time() - start))
    return results


if __name__ == '__main__':
    print(gather_tasks(10))
