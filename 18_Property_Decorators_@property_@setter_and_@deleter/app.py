# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# step 1: Create the product class
class Product:
    def __init__(self, price):
        self.__price = price # Private attributes
    
    @property
    def price(self):
        'Get the price of the product'
        return self.__price
    @price.setter
    def price(self, new__price):
        'Set a new price for the product'
        if new__price < 0:
            raise ValueError('PRice cannot be negative')
        self.__price = new__price
    
    @price.deleter
    def price(self):
        'Delete the price of the product'
        print('Deleting price...')
        del self.__price
# step 2: Create an instance of the product class
product1 = Product(100)
# step 3: GEt the price using the property
print(f'Initial PRice: {product1.price}')
# step 4: Update the price using the setter
product1.price = 150
print(f'UPdated PRice: {product1.price}')
# step 5: Delete the price using the deleter
del product1.price
# step 6: TRy to access the deleted price
try:
    print(product1.price)
except AttributeError as e:
    print(f'Error: {e}')
