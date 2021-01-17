# task4_130121
"""
Task 4
Custom exception
Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file
"""
from datetime import datetime


class CustomException(Exception):
    log_file_name = 'logs.txt'

    def __init__(self, message):
        self.message = message

    def add_log_message(self, message):
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(f'{datetime.today()} : {message} \n')


if __name__ == "__main__":
    except_1 = CustomException('Error 1')
    except_2 = CustomException('Error 2')
    CustomException.add_log_message(except_1, 'Message1')
    CustomException.add_log_message(except_2, 'Message2')



