# task3_200121
"""
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.
"""


def arg_rules(type_: type, max_length: int, contains: list):
    def chek_arg(f):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f'Arg must be {type_}')
                return False
            if len(arg) > max_length:
                print(f'Max length of arg is {max_length}')
                return False
            for c in contains:
                if arg.find(c) < 0:
                    print(f'Arg should contain {contains}')
                    return False
            return f(arg)
        return wrapper
    return chek_arg


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    print(create_slogan('qw05erty@'))

