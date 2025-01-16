# name = "Bob"

# print(f"Hello, {name}")
# name = "Ralf"
# print(f"Hello, {name}")

# Templet.format()
name = "Alex"
greetings= "Hello, {}"
with_name = greetings.format(name);
print(with_name)

longer_pharase= "Hello, {}. Today is {}."
formated = longer_pharase.format("Dude", "Holiday")
print(formated)


