# task2
"""
Writing tests for context manager
Take your implementation of the context manager class from Task 1 and write tests for it.
Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
And also, write tests when your class raises errors or you have errors in the runtime context suite.
"""
import unittest
from task1_060221 import OpenFile


class OpenFileTestCase(unittest.TestCase):
    def setUp(self):
        self.my_open_file_for_read = OpenFile('my_file.txt', 'r')
        self.my_open_file_for_write = OpenFile('my_file.txt', 'w')
        self.my_open_file_for_append = OpenFile('my_file.txt', 'a')

    @staticmethod
    def get_contents_file(file_name):
        with open(file_name) as f:
            file_contests = f.read()
        return file_contests

    def test_open_file_for_read(self):
        with self.my_open_file_for_read as my_f:
            my_file_contests = my_f.read()
        self.assertEqual(my_file_contests, self.get_contents_file('my_file.txt'))

    def test_open_file_for_write(self):
        with self.my_open_file_for_write as my_f:
            my_f.write('Hello\n')
        self.assertEqual('Hello\n', self.get_contents_file('my_file.txt'))

    def test_open_file_for_append(self):
        with self.my_open_file_for_append as my_f:
            my_f.write('World\n')
        self.assertEqual('Hello\n', self.get_contents_file('my_file.txt'))



if __name__ == "__main__":
    unittest.main()
