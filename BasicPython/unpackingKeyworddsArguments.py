def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

def named2(name , age):
    print(name, age)

details = {
    "name": "Bob",
    "age":25
}
named2(**details)

named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for args, value in kwargs.items():
        print(f"{args} : {value}")
    
print_nicely(name = "Bob", age= 27)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

# python divides it automatically positional and names arguments
both(1,2,34, username="bob007", password="12345567")


# another example
# def post(url, data= None, json= None, **kwargs):
#     return request('post', url, data= None, json= None, **kwargs)
# kwargs is basically used to pass arguments from one function to another until they get used 

def my_function(**kwargs):
    print(kwargs)

my_function(**"Bob") ## get a error ** is used only for dictionary must required mapping
my_function(**None) #get an error
