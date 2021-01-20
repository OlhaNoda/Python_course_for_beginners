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
            k = 0
            if isinstance(arg, type_) and len(arg) <= max_length and sum([k+1 for c in contains if c in arg]) == len(contains):
                return f(arg)
            print(f'Arg must be {type_}\nMax length of arg is {max_length}\nArg should contain {contains}')
            return False
        return wrapper
    return chek_arg


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    create_slogan('johndo@05egma')

