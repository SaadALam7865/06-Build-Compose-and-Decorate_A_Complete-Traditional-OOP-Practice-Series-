# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0 # Class variable to keep track of the number of objects created

    def __init__(self):
        Counter.count += 1
        # Incremeent the count each time an object is created

    @classmethod
    def display_count(cls):
        print(f'Number of objects created: {cls.count}')

# Create instances of Counter
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()

Counter.display_count()       

