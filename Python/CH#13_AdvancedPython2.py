#‘pip freeze’ returns all the package installed in a given python environment along with the versions.

#Lambda Functions
square = lambda x: x*x

print(square(6))

#Join Methods
a = ["ABC","XYZ","DEF"]
final = "::".join(a)
print(final)

#Format Methods
b = "{1} is a good {0}".format("ABC", "XYZ")
print(b)

#Map Function
l = [1,2,3,4,5]
sqList = list(map(square,l))
print(sqList)

#Filter Function
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

#Reduce Function
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum,l))