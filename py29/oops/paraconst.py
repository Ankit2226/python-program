class student:
    def __init__(self,name,age,per):
         self.name =name
         self.age =age
         self.per =per
    def display(self):
        print(self.name,self.age,self.per)
obj=student('ankit',19,92)
obj.display()             