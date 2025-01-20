user = {
    "username":"joseph",
    "access_level":"user"
}

# this is the not secure function 
# if you call it anyTime you will get the password
def get_admin_password():
    return "1234"

# make it secure using if
# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"
    
# below print the password
# print(get_admin_password())

# below didn't
# print(secure_get_admin())

# make secure function making it return as a function
# def secure_function(func):
#     if user["access_level"] == "admin":
#         return func

# it will check the function is secure while defining not while calling
# this is isn't enough
# get_admin_password = secure_function(get_admin_password)

# print(get_admin_password())



# using teh decorators 

def make_secure(func):
    def secure_function():
        if user["access_level"] == 'admin':
            return func()
        else:
            return f"No admin permission for user {user['username']}"
        
    return secure_function

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
user = {
    "username":"joseph",
    "access_level":"admin"
}
print(get_admin_password())
