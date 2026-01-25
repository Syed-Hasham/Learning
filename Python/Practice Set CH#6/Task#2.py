a=int(input("Input English Marks:"))
b=int(input("Input Maths Marks:"))
c=int(input("Input Sst Marks:"))

if((a+b+c)/3<33):
    print("You Have Failed!")
if((a+b+c)/3>=33):
    print("You Have Passed!")