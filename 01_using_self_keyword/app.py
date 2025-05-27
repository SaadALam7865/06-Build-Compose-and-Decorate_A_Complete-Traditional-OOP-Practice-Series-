
# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    
    # self keyword is used to access instance variables
    def display(self):
        print(f'Name: {self.name}')
        print(f'Marks: {self.marks}')

student1 = Student('Saad', 85)
student2 = Student('Kaif', 90)

student1.display()
student2.display()