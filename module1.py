# Import print function for python 3.x
from __future__ import print_function

# Print where we are
print(">>> It's First module file")

if __name__ == '__main__':
    print("It's executed by %s" %__name__)
else:
    print("It's executed like a module that directory is %s" %__file__)
