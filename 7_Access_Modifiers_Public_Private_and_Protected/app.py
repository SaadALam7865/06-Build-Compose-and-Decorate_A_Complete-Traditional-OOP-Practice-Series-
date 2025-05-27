# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self,name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
    
    # def get__ssn(self):
    #     return self.__ssn  
    


# Creating an instance of emplpyee
emp = Employee('Saad', 50000, '123-45-6789')
# Accessing public variable
print(f'Public Variable (name): {emp.name}')
# Accessing protected varibale
print(f'Protected Variable (_salary): {emp._salary}')
# Accessing private variable
try:
    print(f'Private Variable (__ssn): {emp.__ssn}')
except AttributeError:
    print(f'Cannot access private variable (__ssn) directly from outside the class. ')
