class Engine:
    def start(self):
        print("Engine has started")

    def stop(self):
        print("Engine has stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

my_car = Car()
my_car.start()
my_car.stop()
