# In packageOne directory, create a file named moduleOne.py:
from packageTwo.moduleTwo import bar, ModuleTwoClass

moduleObj = ModuleTwoClass("Tester")
moduleObj.say_hello()

def foo():
    bar()
    print("Hello from packageOne.moduleOne")