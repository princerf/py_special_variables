# Import print function for python 3.x
from __future__ import print_function

# Import First Module
import module1

# Print where we are
print("\n>>> It's script.py file")

# Print how we executed the script
if __name__ == '__main__':
    print("And it's executed by %s" %__name__)

    print("the module's name is '%s'. It's run from main script" %module1.__name__)
    print(module1.__name__)
else:
    print("It's executed like a module")
