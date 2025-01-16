class Book:
    TYPES = ("hard_cover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"The {self.name}, {self.book_type} has weight {self.weight}"
    
    @classmethod
    def hardcover(cls, book_name, paper_weight):
        return Book(book_name, Book.TYPES[0], paper_weight +100 )
    

    @classmethod
    def paperback(cls, book_name, paper_weight):
        return cls(book_name, cls.TYPES[1], paper_weight)
    # instead of Book.  we can use cls
    

# book = Book("Harry Potter", "hardcover", 1250)
book = Book.hardcover("Harry Potter", 1500)

book2 = Book.paperback("Let us C", 2000)

print(book)
print(book2)
