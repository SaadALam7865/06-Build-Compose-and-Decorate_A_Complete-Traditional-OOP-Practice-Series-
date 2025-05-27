# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0 # Class variable

    @classmethod
    def increment_book_count(cls): # Class method
        cls.total_books += 1
        
        
# Create a new book and increment the count
book1 = Book()
book1.increment_book_count()
book1.increment_book_count()
book1.increment_book_count()
print(f'Total books added: {Book.total_books}')

