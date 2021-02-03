if __name__ == '__main__':

# Homework 16.12.20
# Task2

# 'Hello world'
    print('Hello world')
    print('Hello world')

# '123!456456!789$'
    print('123', 2*'456', '789', sep='!', end='$')
# ' '
    print('\n')

# Task3
# way1
    print(9*'#', 3*'\n#\t\t#', '\n', 9*'#', sep='', end='\n')
    print(2*'\n#\t\t#', '\n', 9*'#', 2*'\n#\t\t#', sep='')

# way2
    print('\n', 9*'#', '#\t\t#', '#\t\t#', '#\t\t#', 9*'#', sep='\n', end='\n\n')
    print('#\t\t#', '#\t\t#', 9*'#', '#\t\t#', '#\t\t#', sep='\n')
