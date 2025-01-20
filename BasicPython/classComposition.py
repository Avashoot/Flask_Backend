# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity
    
#     def __str__(self):
#         return f"BookShelf with {self.quantity} Books."


# shelf =BookShelf(350)
# print(shelf)

# class Book(BookShelf):
#     def __init__(self,name, quantity):
#         super().__init__(quantity)
#         self.name = name
    
#     def __str__(self):
#         return f"Book {self.name}"

# book = Book("Harry Potter", 120)
# print(book)


class Bookshelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return f"{self.name} book."
    

book1 = Book("Harry potter")
book2 = Book("Let us 'C'.")

shelf = Bookshelf(book1,book2)

print(*shelf.books)