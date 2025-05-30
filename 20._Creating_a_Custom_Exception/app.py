# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Step 1: Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message='Age must be 18 or older'):
        self.message = message
        super().__init__(self.message)

# step 2: Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f'Invalid age: {age}. Not allowed under 18.')
    else:
        print(f'Age {age} is valid.✅')

# Step 3: Handle using try...except
try:
    user_Age = int(input('Enter your age: '))
    check_age(user_Age)
except InvalidAgeError as e:
    print(f'Custom Exception Cought: {e}')