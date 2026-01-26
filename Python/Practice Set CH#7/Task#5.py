a = int(input("Enter a number: "))
i=1
sum=0
if(a<1):
        print("Invalid number")
else:
        while(i<=a):
                sum+=i
                i+=1
        print("Sum Of ",a," Natural Numbers: ",sum)
    