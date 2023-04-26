class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # raise NotImplementedError is used as kind of pure virtual function
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

my_dog = Dog("Buddy")
my_cat = Cat("Fluffy")
print(my_dog.speak()) # Output: Woof
print(my_cat.speak()) # Output: Meow
