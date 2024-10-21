class animal:
    def eat(self):
        print("i am animal eating")
    def ani(self):
          print("i am animal")   
class dog(animal):
    def eat(self):
        print("dog is eating")      
        
d=dog()
d.eat()
d.ani()        