# task2_030221
"""
The sys module.
The “sys.path” list is initialized from the PYTHONPATH environment variable.
Is it possible to change it from within Python? If so, does it affect where Python looks for module files?
Run some interactive tests to find it out.
"""
import sys
my_list = sys.path
print(my_list)
