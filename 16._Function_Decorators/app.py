# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

# step:01 define the decorator function
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print('Function is being called')
        return func(*args, **kwargs)
    return wrapper

# step:02 apply the decorator to the function
@log_function_call
def say_hello(name):
    print(f'Hello! {name} ')

@log_function_call
def say_goodbye(text):
    print(f' {text} Saad')
# step:03 call the decorated function
say_hello("saad")
say_goodbye('goodbyee...')

