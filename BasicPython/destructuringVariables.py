x = 3,4,67,5
u, v = 3,6

print(type(x))
print(type(u))
print(u,v)

# friends dictonary
friends_ages = {
    "Bob" : 20,
    "Oggy" : 18,
    "Jack" : 19,
    "Olly" : 18,
    "ShinChan" : 5
}

#  dictonary_name.items() return ([(),()]) a touple inside it a list 
print(friends_ages.items())
# ([(),()]) --> list(didictonary_name.items()) ==> [(),()]
item_list = list(friends_ages.items())
print(type(item_list[0]))

people = [
    ("Bob", 24, "Mechinical Engineer"),
    ("Oggy", 20 , "12th Drop Out"),
    ("Jack", 22, "Persuing the B.Tech.")
]

# iterating through people list through destructuring
for name, age, Education in people:
    print(f"{name} age is {age}, and currently {Education}")


person = ("Olly", 23, "Fashion Designer")

name, _, profession = person

print(name ,_, profession)

# list destructuring
*x, y = [1,2,3,4,5]
print(type(x))
print(type(y))