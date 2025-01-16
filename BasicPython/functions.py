def hello():
    print("Hello Wolrd!!")

hello()

def user_age_in_seconds():
    user_age = int(input("Enter your age : "))
    age_seconds = user_age * 365* 24*60*60
    print(age_seconds)

# user_age_in_seconds()

books = ["Hitler", "Heaven's Door", "Hell's Paradise", "Apple's Work"]

def add_book():
    book_name = input("Enter The Book Name : ")
    # books = books + [book_name] throws the error
    print(books)
    books.append(book_name)
    print(books)

add_book()
