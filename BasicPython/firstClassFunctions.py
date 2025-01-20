def divide(dividend, divisor):
    if(divisor == 0):
        raise ZeroDivisionError("Divisor cannot be 0")
    
    return dividend/divisor

def calculate(*values, operator):
    return operator(*values)

try:
    result = calculate(20,0, operator=divide)
    print(result)
except ZeroDivisionError as e:
    print(e)


def search(sequence, expected, finder):
    for ele in sequence:
        if finder(ele) == expected:
            return ele
    raise RuntimeError(f"Could not find the element with expected {expected}!!")


friends = [
    {"name": "Oggy", "age": 24},
    {"name": "Olly", "age": 23},
    {"name": "Bob", "age": 29},
    {"name": "Jack", "age": 26}
]


def get_friend_name(friend):
    return friend["name"]

# print(search(friends, "Oggy", get_friend_name))
# you can use lambda here

print(search(friends, "Oggy", lambda friend : friend["name"]))






