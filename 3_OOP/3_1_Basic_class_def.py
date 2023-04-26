class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The car has started")

    def stop(self):
        print("The car has stopped")

my_car = Car("Toyota", "Camry", 2021)
print(my_car.make) # Output: Toyota
my_car.start() # Output: The car has started