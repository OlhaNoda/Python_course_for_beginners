# Homework 211220
# task1
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
String = 'Zebra'
if len(String) >= 2:
    print(String[0:2]+String[-2:])
else:
    print('Empty String')

# task2
# The program should check that the string contains only numerical characters and is only 10 characters long
PhoneNumber = '1234567890'
if PhoneNumber.isdigit() and len(PhoneNumber) == 10:
    print('Right format for a phone number')
else:
    print('Wrong format for a phone number')

# task3
# The name check
SavedName = 'olha'
InputName = input('Input your name')
if (InputName.lower()) == SavedName:
    print('The name is correct')
else:
    print('The name is NOT correct')

# task4
# guess the number
# Еще хотела добавить проверку ввода числа
# Если игрок ввел не число, то, чтобы программа сообщала ему об этом и просила ввести ответ корректно
# Начала добавлять проверки в виде циклов и условий, получилось очень громоздко и запутано - убрала это
# Думаю, есть более лаконичный способ проверки ввода данных, и скоро я о нем узнаю ))
from random import randint
start, end = 0, 100
Number = randint(start, end)
AttemptCounter = 1
PlayerNumber = input('Hello! Try to guess the number between 0 and 100! Input it here ')
while int(PlayerNumber) != Number:
    if Number > int(PlayerNumber):
         PlayerNumber = input('You failed. The number is bigger. Try it again! Input your number here ')
         AttemptCounter+=1
    else:
        PlayerNumber = input('You failed. The number is less. Try it again! Input your number here ')
        AttemptCounter += 1
print(f'You guessed it after {AttemptCounter} attempts! Congratulations!')