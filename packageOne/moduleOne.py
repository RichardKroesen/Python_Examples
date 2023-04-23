# In packageOne directory, create a file named moduleOne.py:
from packageTwo.moduleTwo import bar

def foo():
    bar()
    print("Hello from packageOne.moduleOne")