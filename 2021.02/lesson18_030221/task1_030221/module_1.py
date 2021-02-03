def add(*args):
    s = 0
    for number in args:
        s = s + number
    return s


def power_to(power, *args):
    return [number ** power for number in args]
