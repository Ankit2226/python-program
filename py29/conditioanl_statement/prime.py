n=int(input("enter the number : "))
if n==1:
    print("1 is not a prime nuber or not a composite number !")

else:
    i=1
    c=0
    while(i<n):
        
        if n%i==0:
            c +=1
        else:
            c=c
        i+=1

if c>=2:
    print("number is not  a prime !")
else:
    print("number is prime !")            

for i in n:for i in n: