import functools
user = {
    "username": "Joseph",
    "access_level":"guest"
}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for user {user['username']}"
    
    return secure_function


@make_secure
def get_admin_password():
    return "12345"

# print(get_admin_password())
get_admin_password = make_secure(get_admin_password)
print(get_admin_password.__name__)
user["access_level"] = 'admin'
print(get_admin_password())