'''
  *
 ***
*****
'''
a = int(input("Enter a number: "))
for i in range(0,a+1):
    print(" "*(a-i),end ="")
    print("*"*(2*i-1),end ="")
    print("\n")