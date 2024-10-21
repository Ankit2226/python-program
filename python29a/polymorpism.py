class add:  
     def __init__(self, num1, num2):
         print(num1+num2)
     def op(self,n1,n2):
         self.n1=n1
         self.n2=n2
         print("Addition operation",n1+n2)

a=add(2,4)
a.op(4,6)
a.op(10,6)         