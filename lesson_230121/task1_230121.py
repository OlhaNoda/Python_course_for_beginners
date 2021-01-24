# task1_230121
"""
Create a class method named `validate`, which should be called from the `__init__` method
to validate parameter email, passed to the constructor.
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
Email validations:
https://help.xmatters.com/ondemand/trial/valid_email_format.htm
https://en.wikipedia.org/wiki/Email_address
"""


class Person:
    def __init__(self, name, email: str):
        self.name = name
        self.email = email
        Person.validate_email(self.email)

    @staticmethod
    def validate_email(email):
        # Проверка на наличие символа @
        if email.count('@') > 1 or email.count('@') == 0:
            return False, 'Неверное количество символов @'
        # Проверка на наличие точки в доменном имени
        [prefix, domain] = email.split('@')
        if domain.count('.') == 0:
            return False, 'Доменное имя не содержит точки'
        # Проверка длины доменного имени
        if len(domain) < 2:
            return False, 'Доменное имя короче 2 символов'
        # Проверка на наличие точки в начале или конце имени
        if prefix[0] == '.' or prefix[-1] == '.':
            return False, 'Имя начинается или заканчивается точкой'
        # Проверка на наличие двух точек подряд в имени
        dot = False
        for symbol in prefix:
            if symbol == '.':
                if dot:
                    return False, 'Имя содержит две или более точек подряд'
                else:
                    dot = True
            else:
                dot = False
        return True


if __name__ == "__main__":
    p = Person('Steve', 'jj.et@qwerty.com')
    print(p.validate_email(p.email))
