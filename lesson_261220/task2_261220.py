# task2_261220
"""
Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""
import random
random_list_1 = []
random_list_2 = []
common_list_3 = []
i = 0
while i < 10:
    random_list_1.append(random.randint(1, 10))
    random_list_2.append(random.randint(1, 10))
    i += 1
print(f'The list_1 of the random numbers: {random_list_1}')
print(f'The list_2 of the random numbers: {random_list_2}')
print(f'The list_3 with the common numbers: {list(set(random_list_1) & set(random_list_2))}')
