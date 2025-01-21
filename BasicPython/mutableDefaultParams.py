from typing import List, Optional
class Student:
    # never assign a default value to parameters  like grades default  is empty []
    # def __init__(self, name:str, grades: List[int] = []): # this is so bad
    def __init__(self, name:str, grades: Optional[List[int]]=None ): # this is so bad
        self.name = name
        self.grades = grades or []
    

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")

bob.take_exam(90)

print(bob.grades)
print(rolf.grades)