# In package2 directory, create a file named module2.py:

def bar():
    print("Hello from packageTwo.moduleTwo")


class ModuleTwoClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, this is package {self.name}.")