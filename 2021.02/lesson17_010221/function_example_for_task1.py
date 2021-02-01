def make_operations(operator, first_number, *args):
    try:
        return_value = first_number
        if operator in ('+', '-', '*'):
            for number in args:
                if operator == '+':
                    return_value += number
                elif operator == '-':
                    return_value -= number
                else:
                    return_value *= number
            return return_value
        else:
            return False
    except TypeError:
        return False


if __name__ == "__main__":
    make_operations('-', 'u', 8)
