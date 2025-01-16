users = [
    (0, "Bob", "password"),
    (1, "Oggy", "oggy@123"),
    (2, "Jack", "jack@123"),
    (3, "Olly", "olly@123")
]

username_mapping = {
    user[1]: user for user in users
}

print(username_mapping)
print(username_mapping["Olly"])

username_input = input("Enter the username :")

password_input = input("Enter the Password :")

_, username, password = username_mapping[username_input]

if password == password_input:
    print("Logged is successful !!")
else : 
    print("Incorrect credentials")