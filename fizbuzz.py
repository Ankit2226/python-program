print("welcome to game")
i=1
for i in range(i,101):
  
     if(i%3==0 and i%5==0):
       print("fizzbuzz",i)
     elif(i%5==0):
         print("buzz",i)
     elif(i%3==0 ):
         print("fizz",i)
     else:
      print(i)
     