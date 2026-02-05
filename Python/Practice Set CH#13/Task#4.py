n = [6,10,25,7,5,110,64,32,65,66]
div5 = lambda x : x % 5 == 0
print(list(filter(div5,n)))