print("Assignment & Datatypes")
#Variables are case sensitive
#Datatypes are assigned automatically
#Datatypes can also be assigned using casting
a = 30
print("A =",a,"(Integer)")
b = float(2.33)  #Casting
print("B =",b,"(Floating point)")
c = "XYZ"
print("C =",c,"(String)")
d = False
print("D =",d,"(Boolean)")
e = None
print("E =",e,"(None)")
print("\nDatatypes can also be returned with the type() function.")
print("\nA is ",type(a),"\nB is ",type(b),"\nC is ",type(c),"\nD is ",type(d),"\nE is ",type(e))

print("\nOperators")
print("\n= is the assignment operator")
print("\nA+B=",a+b,"Addition")
print("A-B=",a-b,"Subtraction")
print("A*B=",a*b,"Multiplication")
print("A/B=",a/b,"Division")
print("\n+= increments the value of a variable by the number given")
print("\n-= decrements the value of a variable by the number given")

print("\nComparison Operators")
print("\nA==B:", a==b, "Checks if A is equal to B")
print("A!=B:", a!=b, "Checks if A is not equal to B")
print("A>B:", a>b, "Checks if A is greater than B")
print("A<B:", a<b, "Checks if A is less than B")
print("A>=B:", a>=b, "Checks if A is greater than or equal to B")
print("A<=B:", a<=b, "Checks if A is less than or equal to B")

print("\nLogical Operators")
print("\nLogical operators are used to combine conditional statements.")
print("\nA > 10 and B < 5:", a > 10 and b < 5, "Returns True if both conditions are true")
print("A > 10 or B < 5:", a > 10 or b < 5, "Returns True if at least one condition is true")
print("not(A > 10):", not(a > 10), "Returns True if the condition is false")

print("\nCasting")
x=str(a)
print("Casting an integer to a string:", x, "is a",type(x))
x=float(a)
print("Casting an integer to a float:", x, "is a",type(x))
x=int(b)
print("Casting a float to an integer:", x, "is a",type(x))

print("\nInput")
y=input("Give Input: ")
print("You entered: ",y,"\t",type(y))