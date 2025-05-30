# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

# step: 01 CReate the Multiplier class
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor
    
# step 2: Create an instance of multiplier
multiplier = Multiplier(3)
# step 3: Check if the instance is callable
print(f'Is multiplier callable? {callable(multiplier)}') # Sould return True
# step 4: USe the instance like a  function
result = multiplier(5) # Jab object call hoga, yeh method chalega
print(f'REsult of multiplying 5 by factor 3: {result}')
