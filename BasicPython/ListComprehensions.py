nums = [1,2,4,5,6,7,33]
doubled = []

# traditional way
for i in nums:
    doubled.append(i*2)

print(doubled)

# comprehension
doubles = [x*2 for x in nums]
print(doubles)


friends = ["Bob", "Big-Bo", "Rasta", "Tiger", "Joe", "Brook", "Brand"]
starts_b = []
for friend in friends:
    if friend.startswith("B"):
        starts_b.append(friend)

print(starts_b)

# comprehension
starts_with_b = [friend for friend in friends if friend.startswith("B")]

print(starts_with_b)
