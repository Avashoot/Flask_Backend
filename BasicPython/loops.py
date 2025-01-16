# number guessing game
import random

number = random.randint(1,100)

user_input = input("Would you like to play ? (Y/n)\n").lower()

if user_input == "y":
    while(user_input == "y") :
        
        user_number = int(input("Start Guesing : "))
        if user_number == number :
            print("Congratulations, your guess is right, you Win!!")
            break
        elif user_number < number :
            print("Your guess is low think higher")
        else:
            print("Your guess is high think lower")
        
        user_input = input("Would you like to paly or quit? (Y/n) : ")


# for loop
friends = ["Bob", "Oggy", "Jack", "Olly"]

for friend in friends:
    print(f"{friend} is my friend")


nums = [ 23,34,5,45,6,5,6,7,66,5,343,4 ]
total = 0
lenth = len(nums)

for i in nums:
    total += i
print(total/lenth)

