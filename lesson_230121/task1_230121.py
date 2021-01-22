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

    @classmethod
    def validate_email(cls, email):
        if email.count('@') > 1 or email.count('@') == 0:
            return False, 'Неверное количество знаков @'
        return True


if __name__ == "__main__":
    p = Person('Steve', 'etetet@@ururu')
    print(p.validate_email(p.email))
