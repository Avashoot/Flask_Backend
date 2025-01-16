class ClassTest:
    def instance_method(self):
        print(f"you call the instance_method of {self}")
    
    def __str__(self):
        return "ClassTest class"
    
    @classmethod
    def class_method(cls):
        print(f"you are calling the class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"You are calling the static_method")
    

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()