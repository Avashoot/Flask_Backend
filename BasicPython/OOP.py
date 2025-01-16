std ={
    "name" : "Oggy",
    "grades" : (89,92,97,99,85,86)
}

def average(sequence):
    return sum(sequence)/len(sequence)

print(average(std["grades"]))

# use OOPs

class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (89,92,97,99,85)

    def average(self):
        return sum(self.grades)/len(self.grades)
    

student = Student()
print(student.name)
print(student.grades)

print(Student.average(student))
    # ⬆️ instead of calling like this 
    # ⬇️ call the method on object directly
print(student.average())


class Student2:
    # act like constructor
    # self act like 'this' keyword in java
    def __init__(self, name , grades):
        self.name = name
        self.grades = grades
    
    def average_grades(self):
        return sum(self.grades)/len(self.grades)
    
    def print_data(self):
        print(f"{self.name} get {self.average_grades()}%")
    

std1 = Student2("Bob", (89,92,97,99,85))
std1.print_data()

std2 = Student2("Oggy", (100,99,88,99,85))
std2.print_data()

