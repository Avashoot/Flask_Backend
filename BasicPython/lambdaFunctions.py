def add(x,y):
    return x+y

print(add(3,7))

add = lambda x, y : x+y

print(add(10,20))
print(add(30,40))

print((lambda x, y : x==y)(10,11))

def double(x):
    return x*2

sequence = [2,4,6,8,4,2,7]

doubled_list_comprehension = [x*2 for x in sequence]
print(doubled_list_comprehension)
# does the same thing as above x*2 act as lambda function
doubled_using_function = [double(x) for x in sequence]
print(doubled_using_function)

doubled_using_map = list(map(lambda x: x*2, sequence))
print(doubled_using_map)