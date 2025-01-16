def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total

mul_value = multiply(1,2,4,5,6)
# print(mul_value)
# print(multiply(-1))
"Avadhoot"
def add(x,y):
    print(x,y)
    return x+y

nums = [3,4]
print(add(*nums))

a, b = ([34,45], [34])
# print(a)

data = {"x": 13, "y": 12}

# print(add(data["x"], data["y"]))
print(add(**data))


def apply(*args, operator):
    if(operator == "*"):
        return multiply(*args)
    if(operator == "+"):
        return sum(args)
    else:
        return "No valid operator is provided to apply()."


print(apply(112,34,5,4,5,6,5,4, operator="*"))

tpl = (1,2,3,45,54)
print(multiply(*tpl))