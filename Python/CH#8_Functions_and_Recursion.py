def function():
    print("Hello")

function()

#FUNCTIONS WITH ARGUMENTS
def sayhello(name):
    return "Hello " + name

print(sayhello("XYZ"))

#DEFAULT PARAMETER VALUE
def sayhello(name="Default"):
    return "Hello " + name

print(sayhello())

#RECURSION
def factorial(n):
    if n == 0 or n==1: 
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(4))
