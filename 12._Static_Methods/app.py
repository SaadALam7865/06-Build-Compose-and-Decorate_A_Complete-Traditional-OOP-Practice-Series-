# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConvertor:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Exampleusage:
obj1 = TemperatureConvertor()
print(obj1.celsius_to_fahrenheit(12))
    
    
