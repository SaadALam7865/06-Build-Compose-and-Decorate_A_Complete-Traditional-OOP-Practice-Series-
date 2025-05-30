# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print('A show method')

class B(A):
    def show(self):
        print('B show method')
class C(A):
    def show(self):
        print('C show method')

class D(B, C):
    pass

# Create an object of D and call show()
d = D()
d.show() # Output: D show method
# To observe MRO
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# The MRO shows the order in which classes are searched when a method is called.