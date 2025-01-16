class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person is {self.name} and his age is {self.age}"
    
    def __repr__(self):
        return f"Object looks like name : {self.name} and age : {self.age}"
    
bob = Person("Oggy", 35)
print(bob.name)
print(bob.__repr__)