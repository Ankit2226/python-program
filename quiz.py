import random
import math

name=input("enter your name ")
print("welcome to quiz!",name)
temp=random.randint(1,2)

score=0
a=1
while(a==1):
     #square
    if(temp==1):
      num=random.randint(1,10)
      print("what is the square of",num,":")   
      ans=(int)(input("Guess your answer :"))
      square=num*num
      if square == ans:
         print("your answer correct !")
         score=score+1
      else :
        print("your answer wrong correct answer is :",square)
    else:
       num=random.randint(1,100)
       print("what is the square of",num**2,":")     
       num2=(int)(input("Guess your answer :"))
       sqrt = math.sqrt(num)
       if (num== num2):
          print("your answer correct !")
          score=score+1

       else :
          print("your answer wrong !correct answer is :",sqrt)
     
    if(score>3):
       print("you are excellant !")
    elif(score>=1 ):
       print("you are pass !")
    else:
       print("you are fail !")

    print("Do you want to continue y=1 or n=0 !")
    a=int(input(" your choise :"))
