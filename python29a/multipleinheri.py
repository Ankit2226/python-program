class Dypschool:
    def sname(self):
         print("this is  DYP school >>>> ")
class Dpclg:
    def cname(self):
        print("this is DYP CLG >>>>>>")
        
class dypgroup(Dypschool,Dpclg):
     def dypGroup(self):
        print("this is dyp group !!")                
dyp =dypgroup()
dyp.sname()
dyp.cname()
dyp.dypGroup()
         
        