import functools



def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        return func(*args, **kwargs)
    
    return secure_function


@make_secure
def get_password(panel):
    if panel == 'admin':
        return "12345"
    elif panel == 'billing':
        return "super secure password"

# print(get_admin_password())
get_password = make_secure(get_password)
print(get_password.__name__)
print(get_password('billing'))