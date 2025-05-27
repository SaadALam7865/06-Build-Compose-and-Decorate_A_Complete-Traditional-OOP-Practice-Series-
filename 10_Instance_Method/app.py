# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self): # Instance methods
        print(f'{self.name} says woof! I am a {self.breed}.')

# Create an instance of Dog and call the bark method
my_dog = Dog('Tommy!', 'Golden Retriver')
my_dog.bark() 