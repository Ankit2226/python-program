## 1st
def name():
    print("hi good morning ! ")

name()

def greet(name):
     return f"hello ,{name} !"
print(greet("Ankit"))


## 2nd
def power(base,exponent=2):
     return base * exponent

print(power(3))
print(power(3,3))

## 3rd
def sum_all(*args):
     return sum(args)
   
print(sum_all(1,2,3,4,5))   

print(sum_all(10,20))

##print info 

def print_info(**kwargs):
     for key,value in kwargs.items():
        print(f"{key}:{value}")

print_info(name="patil",)


##
numbers =[1,2,3,4,5]
squared= list(map(lambda X: X**2,numbers))
print(squared)

#outer inner
def outer(x):
     def inner(y):
          return x+y
     return inner
add_5 =outer(5)
print(add_5(3))