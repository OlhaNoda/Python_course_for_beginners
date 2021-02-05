# task1
"""
Task 1
File Context Manager class
Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method,
which has to cover all the requirements to context managers mentioned here:
"""
from datetime import datetime
log_file = 'logs.txt'
text_file = 'my_file.txt'


class OpenFile:

    def __init__(self, file_name, action):
        self.file_name = file_name
        self.action = action
        self.logs = open('logs.txt', 'a')

    def log_open_file(self):
        return self.logs.write(f'{datetime.now()}: {self.file_name} was opened for {self.action}\n')

    def log_close_file(self):
        return self.logs.write(f'{datetime.now()}: {self.file_name} was closed\n')

    def __enter__(self):
        self.f = open(self.file_name, self.action)
        self.log_open_file()
        return self.f

    def __exit__(self, exp_type, exp_value, exp_tr):
        self.log_close_file()
        self.f.close()
        self.logs.close()


if __name__ == "__main__":
    with OpenFile(text_file, 'w') as f:
        f.write('Hello\n')

    with OpenFile(text_file, 'a') as f:
        f.write('World\n')

    with OpenFile(text_file, 'r') as f:
        f.read()
