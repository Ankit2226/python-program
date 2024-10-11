class Emp:
    #initialization 
    def __init__(self,name,id):
        print("employee created !!",name,id)
    def __del__(self):
        print("employee deleted !!",name,id)    
em=Emp("ankit",1)
#em1=emp("harsh",2)
