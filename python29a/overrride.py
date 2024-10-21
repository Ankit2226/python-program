class override:
    def priname(self,name):
        self.name=name
        print("hi name is ",name)
class run(override):
    def priname(self,name):
        print(" hi i am",name)
r=run()
r.priname("ankit")
        