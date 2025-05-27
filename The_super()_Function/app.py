# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

# Inheriting the Person class
class Teacher(Person):
    def __init__(self,name, subject):
        super().__init__(name)
        self.subject = subject
    
    # display method to show the details of the teacher
    def display(self):
        print(f'Teacher Name: {self.name}, Subject: {self.subject}')

# CReating an instance of teahcer
teacher = Teacher(' Sir Saad', 'Python Programming')
# Displaying the details of the teacher
teacher.display()
