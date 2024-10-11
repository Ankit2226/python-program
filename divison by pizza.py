
class divisionByPizza(Exception):
    pass
def divide(a,b):
      if b=="ankit":
           raise divisionByPizza("can't divide by ankit !")
      return a/b

try:
    result=divide(2,"ankit")
except  divisionByPizza as e:
          print(e)

