import os

my_file = 'test.txt'

# Non-Pythonic way
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File can\'t be accessed')

# Pythonic way EAFP
try:
    f = open(my_file)
except IOError as e:
    print('File can\'t be accessed')
else:
    with f:
        print(f.read())