list=["um","hello","um","my name is ","um","ankit","um","um"]
count=0

def check(word):
   if(word=="um"):
    count=count+1

for word in list :
     check(word)
  
print(count)    

def count_ums(speech):
   print(" ")