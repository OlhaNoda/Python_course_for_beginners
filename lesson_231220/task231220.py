# Homework 231220
# task1
'''
The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
'''
from random import randint
start, end = 0, 10
number = randint(start, end)
player_number = input('Hello! Try to guess the number between 0 and 10! Input it here ')
if player_number == str(number):
    print(f'You won! Congratulations!')
else:
    print(f'You failed. The number is {number}')

# task2
'''
The birthday greeting program.
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”
'''
name = input('Input your name ')
age = input('Input your age by numbers ')
if age.isdigit():
    print(f'Hello {name}, on your next birthday you’ll be {int(age)+1} years')
else:
    print('Entered age is wrong')

# task4
'''
The math quiz program
Write a program that asks the answer for a mathematical expression,
checks whether the user is right or wrong, and then responds with a message accordingly.
'''
import random
a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
action1, action2 = random.choice(['+', '-', '*']), random.choice(['+', '-', '*'])
if action1 == '+' and action2 == '+': result = a+b+c
elif action1 == '+' and action2 == '-': result = a+b-c
elif action1 == '+' and action2 == '*': result = a+b*c
elif action1 == '-' and action2 == '-': result = a-b-c
elif action1 == '-' and action2 == '+': result = a-b+c
elif action1 == '-' and action2 == '*': result = a-b*c
elif action1 == '*' and action2 == '*': result = a*b*c
elif action1 == '*' and action2 == '+': result = a*b+c
else: result = a*b-c
user_result = int(input(f'Try to solve the problem: {a} {action1} {b} {action2} {c}\n'))
if user_result == result:
    print('You did it! Congratulations!')
else:
    print('You made a mistake :(')

# task5
'''
Спросили у пользователя предел и от нуля до предела выводим(принтуем) все числа кроме кратных 18ти.
На числе 42 принтуем "Потому что".  Числа от 50ти до 80ти игнорируем.
'''
limit = int(input('Input the limit '))
number = 0
while number != limit:
    if number % 18 != 0 and number != 42 and number < 50 or number > 80:
        print(number)
    elif number == 42:
        print('because')
    else:
        pass
    number += 1

# task6
'''
Спросить у пользователя сколько попыток и до скольки максимум пробовать.
Сделать генерацию рендомного значения столько то раз.
Каждое значение вывести и потом вывести итоговое максимально выпавшее число.
'''
import random
tries = int(input('How many tries? '))
limit = int(input('Until when to try? '))
t = 1
value = 0
max_value = 0
while t != tries+1:
    value = random.randint(1, limit)
    print('Random value', t, ':', value)
    if value > max_value:
        max_value = value
    else:
        pass
    t += 1
print('Max value:', max_value)

# task7
'''
пишем в цикле решение уравнения аХ**2+bx+c=0 рассчитываем ответ.
'''
import random
import math
a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
print(f'Solution of the problem {a}x**2+{b}x+{c}=0)')
discr = b**2-4*a*c
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f'Discriminant={discr}, x1={x1}, x2={x2}')
elif discr == 0:
    x = -b / (2 * a)
    print(f'Discriminant={discr}, x={x}')
else:
    print('The equation has no solution')

# task8
'''
камень-ножницы-бумага пока не надоест (Q) загадываем и спрашиваем пользователя что он загадал.
Плюсуем себе или ему победу и так по кругу. Принтуем общий счет.
'''
import random
quantity = int(input("Let's play rock, paper, scissors! Input how many times you want to play: "))
t = 0
comp_counter = 0
player_counter = 0
while t != quantity:
    player = input('Choose rock, paper or scissors by typing r, p or s: ')
    if player == 'r' or player == 'p' or player == 's':
        computer = random.randint(1, 3)
        if computer == 1: print(f'Computer: r')
        elif computer == 2: print(f'Computer: p')
        else: print(f'Computer: s')
        if (computer == 1 and player == 'r' or computer == 2 and player == 'p' or computer == 3 and player == 's'):
            comp_counter += 1
            player_counter += 1
            print(f'It is a draw. Score: computer {comp_counter} : player {player_counter}')
        elif (computer == 1 and player == 'p' or computer == 2 and player == 's' or computer == 3 and player == 'r'):
            player_counter += 1
            print(f'You win! Score: computer {comp_counter} : player {player_counter}')
        else:
            comp_counter += 1
            print(f'You lost. Score: computer {comp_counter} : player {player_counter}')
    else:
        print('Your input was in the wrong format')
    t += 1
if player_counter > comp_counter:
    print(f'GAME OVER. Congratulations! You win! Score: computer {comp_counter} : player {player_counter}')
elif player_counter < comp_counter:
    print(f'GAME OVER. You lost. Score: computer {comp_counter} : player {player_counter}')
else:
    print(f'GAME OVER. It is a draw. Score: computer {comp_counter} : player {player_counter}')
