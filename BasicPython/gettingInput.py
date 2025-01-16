name = input("Enter yout name : ")
print(name)

#input always return a string
size_input = input("How big is your house (in square feet) : ")
square_feet = int(size_input)
square_meter = square_feet//10.8
print(f"{square_feet} square feet is {square_meter} square meters.")