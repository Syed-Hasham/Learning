n = []
for i in range(4):
    n.append(int(input("Enter Number:")))

if(n[0]>n[1] and n[0]>n[2] and n[0]>n[3]):
    print(n[0],"is the greatest")
elif(n[1]>n[0] and n[1]>n[2] and n[1]>n[3]):
    print(n[1],"is the greatest")
elif(n[2]>n[0] and n[2]>n[1] and n[2]>n[3]):
    print(n[2],"is the greatest")
else:
    print(n[3],"is the greatest")
