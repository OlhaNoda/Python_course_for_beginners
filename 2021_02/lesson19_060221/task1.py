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
text_file = 'file1.txt'


class OpenFile:

    def __init__(self, file_name, action, log_file_name):
        self.file_name = file_name
        self.action = action
        self.log_file_name = log_file_name

    def logging_open_file(self):
        self.logs = open(self.log_file_name, 'a')
        return self.logs.write(f'{datetime.now()}: the file {self.file_name} was opened for {self.action}\n')

    def logging_close_file(self):
        self.logs = open(self.log_file_name, 'a')
        return self.logs.write(f'{datetime.now()}: the file {self.file_name} was closed\n')

    def __enter__(self):
        self.f = open(self.file_name, self.action)
        self.logging_open_file()
        return self.f

    def __exit__(self, exp_type, exp_value, exp_tr):
        self.logging_close_file()
        self.f.close()
        self.logs.close()


with OpenFile(text_file, 'w', log_file) as f:
    f.write('Hello\n')

with OpenFile(text_file, 'a', log_file) as f:
    f.write('World\n')

with OpenFile(text_file, 'r', log_file) as f:
    f.read()
