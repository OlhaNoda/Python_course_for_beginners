# task2_170221
"""
Write a program that reads in a sequence of characters,
and determines whether it's parentheses, braces, and curly brackets are "balanced."
f('[()]{}{[()()]()}') -> Balanced
f('[(])') -> Not Balanced
"""


def chek_brackets_balanced(sequence_of_char: str):
    stack = []
    for char in sequence_of_char:
        if char in ['(', '{', '[']:
            stack.append(char)  # добавляем в стек открывающие скобки по очереди их появления в выражении
        else:
            if not stack:
                return False
            # забираем из стека открывающую скобку добавленную туда последней
            last_opening_bracket = stack.pop()
            # сравниваем ее с ближайшей закрывающей скобкой
            if last_opening_bracket == '(':
                if char != ")":
                    return False
            if last_opening_bracket == '{':
                if char != "}":
                    return False
            if last_opening_bracket == '[':

                if char != "]":
                    return False
    if stack:  # в стеке останутся значения, если открывающих скобок больше, чем закрывающих
        return False
    return True


if __name__ == '__main__':
    sequence_of_brackets = '([{}'
    if chek_brackets_balanced(sequence_of_brackets):
        print(f'The expression {sequence_of_brackets} is balanced')
    else:
        print(f'The expression {sequence_of_brackets} is not balanced')
