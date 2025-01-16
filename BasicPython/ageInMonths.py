user_age = int(input("Enter your age : "))
age_in_months = user_age * 12
print(f"Your age {user_age} is equal to, {age_in_months} months.")
# age in seconds
# There are 3600 seconds in one hour datily 24 hrs = 3600*24
# There are 365 days in each year 
# one leap year after 3 years = age// 4 we get the leap years i.e no. of extra days

no_leap_years = user_age // 4
age_in_seconds = (365 + no_leap_years)*24*3600
print(f"Your age {user_age} is equal to, {age_in_seconds} seconds")
