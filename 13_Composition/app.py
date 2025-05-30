# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self): # class method of Engine
        print('Engine has started...')

class Car:
    def __init__(self):
        self.engine = Engine() # composition: CAr has an angine

    def start_car(self):
        print('Car is starting...')
        self.engine.start()

my_car = Car()
my_car.start_car()