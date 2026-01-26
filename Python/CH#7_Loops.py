print("While Loops")
i = 1
while(i<6):
    print(i)
    i+=1

print("For Loops")
for a in range(1,6): #Step size can also be given
    print(a)

print("For in Loop") # can alos be used to iterate strings
l = [1,4,67,7,4,31]
for b in l:
    print(b)

print("For Else Loop")
for item in l:
    print(item)
else:
    print("done")

print("Break Statement")
for c in range(6):
    if(c==3):
        break #Breaks Out of the loop
    print(c)

print("Continue Statement")
for c in range(6):
    if(c==3):
        continue #Skip this iteration
    print(c)

print("Pass Statement")
for item in l:
    pass # without pass, the program will throw an error, a null statement