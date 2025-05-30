# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

# step 01: CReate a Countdown class
class Coundown:
    def __init__(self,start):
        self.current = start
    
    def __iter__(self):
        return self  # Object is its own iterator
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration # Signal end of iteration
        else:
            val = self.current
            self.current -= 1
            return val
import time    
# Test it with a for loop
for num in Coundown(5):
    time.sleep(0.5)
    print(num)

    

