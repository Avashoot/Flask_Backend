import functools

user ={
    'username':'jack',
    'access_level': 'guest'
}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f"NO {access_level} permission for user {user['username']}"
        
        return secure_function 
    
    return decorator

@make_secure('admin')
def get_admin_password():
    return 'admin : 12345'

@make_secure('user')
def get_dashboard_password():
    return 'user : user_password'


print(get_admin_password())
print(get_dashboard_password())

user ={
    'username':'Olly',
    'access_level': 'admin'
}


print(get_admin_password())
print(get_dashboard_password())


user ={
    'username':'Bob',
    'access_level': 'user'
}


print(get_admin_password())
print(get_dashboard_password())