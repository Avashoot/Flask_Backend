friends_ages = {
    "Bob" : 20,
    "Oggy" : 18,
    "Jack" : 19,
    "Olly" : 18,
    "ShinChan" : 5
}

print(friends_ages)
friends_ages["Bob"] = 24
print(friends_ages)

print(friends_ages["Olly"])


frineds = [
    {"Name" : "Bob", "age" : 24},
    {"Name" : "Oggy", "age" : 18},
    {"Name" : "Jack", "age" : 20},
    {"Name" : "Olly", "age" : 18}
]

print(frineds[0]["Name"])

# Iterate over dictonary
for i in friends_ages:
    print(f"{i} : {friends_ages[i]}")

for student, age in friends_ages.items():
    print(f"{student} : {age}")

# get values only
age_values = friends_ages.values()
print(sum(age_values))

# check key is avilable
if "Oggy" in friends_ages:
    print("Avilable")
else : 
    print("Not Avilable")