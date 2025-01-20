def add(x, y):
    result = x+y
    print(result)

add(10,20)

def say_hello(name, surname):
    print(f"Hello, {name} {surname}!!")

say_hello("Cuddy", "Smith")

say_hello(surname= "Rock", name="Smith")

#  divide

def divide(numerator, denominator):
    if denominator != 0:
        print(f"Value is {numerator/denominator}")
    else:
        print("Cannot divide by zero")

divide(201,30)

divide(10,10)