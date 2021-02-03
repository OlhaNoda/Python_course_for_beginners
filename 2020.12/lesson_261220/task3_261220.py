# task3_261220
"""
Extracting numbers.
Make a list that contains all integers from 1 to 100,
then find all integers from the list that are divisible by 7 but not a multiple of 5,
and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
"""
main_list = list(range(1, 100))
sample_list = []
i = 0
while i < len(main_list):
    if main_list[i] % 7 == 0 and main_list[i] % 5 != 0:
        sample_list.append(main_list[i])
    i += 1
print(sample_list)
