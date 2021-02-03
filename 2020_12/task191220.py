# Homework 19.12.20
# Task1
# “Good day <name>! <day> is a perfect day to learn some python.”
name = 'Olha'
day = '19.12.20'
print('Good day ', name, '! ',  day, ' is a perfect day to learn some python.', sep='')

print(f'Good day {name}! {day} is a perfect day to learn some python.')

welcome = 'Good day <name>! <day> is a perfect day to learn some python.'
print(welcome[0:9], name, welcome[15:17], day, welcome[22:], sep='')

# Task2
# Concatenation
name ='Olha'
lastname = 'Noda'
print(name+' '+lastname)

# Task3
# Using python as a calculator
a = 7
b = 2
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)
print(a%b)
print(a//b)

# task4
# вывести из слова 'Корован' слово 'ворона'
S1 = 'Корован' [::-1]
print(S1[2:6]+S1[0:2])
