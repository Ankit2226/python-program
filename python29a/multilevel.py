class grandparent:
    def gpname(self):
        print(" i am grandparent !" )
        
class parent(grandparent):
    def pname(self): 
       print("i am parent !")
class iam(parent):
    def myname(self):
        print("my name is me !")
class child(iam):
    def cname(self):
        print("i am child !!!")  
ch=child()
ch.gpname()
ch.pname()
ch.myname()                                            