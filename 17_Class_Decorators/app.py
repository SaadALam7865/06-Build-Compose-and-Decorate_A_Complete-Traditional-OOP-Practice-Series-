# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


# Step 1: Class Decorator
def add_greeting(cls):
    def greet(self):
        return 'Hello from Decorator!'
    cls.greet = greet # Add greet method to the class
    return cls # REturn the modified class

# STep 2: Apply the decorator to a class
@add_greeting
class Person:
    def __init__(self,name):
        self.name = name # clss attribute/instance attributs

# step 3: CReate an instance and call the greet method
person = Person('Muneeb Ali')
print(person.greet())
