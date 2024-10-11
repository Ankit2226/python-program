import math
import random
randomno=(random.randint(2,16))
a=16
print("the guess square root of :",randomno)

correct=(int)(input("Guess your answer :"))
sqrt = math.sqrt(a)

if(sqrt==correct):
    print("guess is correct")
else:
    print("guess is wrong")    