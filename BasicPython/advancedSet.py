friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local = friends.difference(abroad)

# print(local)
# print(abroad.difference(friends))

# print(local.union(abroad))

art = {"Bob", "Jen", "Charlie", "Rolf"}
Science = {"Bob", "Jen", "Adam", "Anne"}

art_only = art.difference(Science)
print(art_only)

Science_only = Science.difference(art)
print(Science_only)

both = art.intersection(Science)
print(both)

total_students = art.union(Science)
print(total_students)

