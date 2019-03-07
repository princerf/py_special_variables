# Import print function for python 3.x
from __future__ import print_function

# Print where we are
print(">>> It's script.py file")

# Print how we executed the script
if __name__ == '__main__':
    print("And it's executed by %s" %__name__)

    # Import First Module
    import module1

else:
    print("It's executed like a module")
