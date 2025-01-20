def divide(numerator, denominator):
    # if denominator ==0:
    #     print("Denominator cannot be 0.")
    #     return
    if denominator ==0:
        raise ZeroDivisionError("Denominator cannot be 0.")
    
    return numerator/denominator


# grades:list = []

# print("Welcome to the average grade program.")
# try:
#     average = divide(sum(grades), len(grades))
#     # print(f"The average grade is {average}")
# except ZeroDivisionError as e:
#     print(f"There are no grades yet in your list ({e})")
# else:
#     print(f"The average grade is {average}")
# finally:
#     print("This is always get executed if there is error or not")

students =[
    {"name": "Bob", "grades": [70,75]},
    {"name": "Oggy", "grades": [24]},
    {"name": "Jack", "grades": [90,95]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades")
else:
    print("--All Students average is calculated--")
finally:
    print("--End of student average calculation--")



