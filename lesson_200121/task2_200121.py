# task2_200121
"""
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""
StopList = ['pepsi', 'BMW']


def stop_words(words: list):
    def replace_word(func):
        def wrapper(*args):
            text = func(*args)
            for word in words:
                text = text.replace(word, '*')
            return text
        return wrapper
    return replace_word


@stop_words(StopList)
def create_slogan(name: str, lastname: str):
    return f"{name} {lastname} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    print(create_slogan('Steve', 'Smith'))
