# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,name):
        self.name = name  # independent existence

class Department:
    def __init__(self, employee):
        self.employee = employee # aggregation
    
    def show_employee(self):
        print(f'Empleyee in department: {self.employee.name}')

emp = Employee('Saad') # Employee exists independently
dept = Department(emp)  # Department holds a reference to Employee
dept.show_employee()  # output: Employee in department: Saad

del dept
print(emp)
