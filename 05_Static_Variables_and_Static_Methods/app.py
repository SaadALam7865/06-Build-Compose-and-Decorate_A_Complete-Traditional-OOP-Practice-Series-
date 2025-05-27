# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
    

obj1 = MathUtils()
print(obj1.add(2, 3))
