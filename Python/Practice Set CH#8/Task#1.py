def greatestval(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
    
a=input("A: ")
b=input("B: ")
c=input("C: ")
print(greatestval(a,b,c))
