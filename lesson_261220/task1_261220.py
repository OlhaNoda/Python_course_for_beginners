# task1_261220
'''
The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
'''
import random
random_list = []
i = 0
while i < 10:
    random_list.append(random.randint(1, 10))
    i += 1
print(f'The list of random the numbers: {random_list}')
print(f'The largest number from the list: {max(random_list)}')
