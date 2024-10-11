import random
randomno=(random.randint(1,10))

print("the randonm number selected is :",randomno)

correct=(int)(input("Guess your answer :"))
square =randomno*randomno
if(square==correct):
    print("guess is correct")
else:
    print("guess is wrong")    