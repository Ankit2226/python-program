class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, dob):
        super().__init__(name, age)  
        self.dob = dob

    def displayinfo(self):
        print(self.name, self.age, self.dob)

obj = Student("ankit", 19, 15)
obj.display()
obj.displayinfo()