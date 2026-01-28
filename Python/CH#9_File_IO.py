print("\nREADING FROM FILE\n")
f = open("file.txt")
data = f.read()
print(data)
f.close()

print("\nWRITING TO FILE\n")
str="HELLO"
f=open("file2.txt","w")
f.write(str)
f.close()

print("\nREADLINES FUNCTION\n")

f=open("file3.txt")
lines = f.readlines()
print(lines)
f.close()

print("\nREADLINE FUNCTION\n")
f=open("file3.txt")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)
# f.close()

# OR SIMPLY USE
line = f.readline()
while(line!=""):
    print(line)
    line = f.readline()
f.close()

print("\nAPPEND MODE\n")
f=open("file4.txt","a")
f.write(str)
f.close()

print("\nWITH STATEMENT\n")
#NO NEED TO CLOSE FILE ISING WITH STATEMENT
with open("file.txt") as f:
    print(f.read())