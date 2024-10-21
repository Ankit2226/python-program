class vec:
    def ve(self):
        print("this is vechicle !! ")
class car(vec):
    def fourwheeler(self):
        print("this is car !!")
class twowheelr(car):
    def two(self):   
       print("two wheeler !!")     
class hybridvechicle(twowheelr):
    def hybrid(self):        
       print(" hybrid vehicle !!") 
v=hybridvechicle()     
v.ve()
v.fourwheeler()
v.two()
v.hybrid()              