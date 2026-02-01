n = int(input("Enter Number:"))
table = [n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(str(table)+"\n")
