#Lists are Mutable
#lists can store any datatypes
#lists are indexed like strings
print("Lists")
abc = ["apple",12.44444,123,True]
print(type(abc))
print(abc)
print("\n",abc[0])
print("\n",abc[1])
print("\n",abc[2])
print("\n",abc[3])

print("\nList Methods")

print("\nlist.sort()")
l1 = [1,3,4,7,6,8,2]
l1.sort()
print(l1)

print("\nlist.reverse()")
l1.reverse()
print(l1)

print("\nlist.insert()")
l1.insert(0,61)
print(l1)

print("\nlist.append()")
l1.append(9)
print(l1)

print("\nlist.pop()")
#if parameters left empty it will remove the last index
#enter index of value in parameter to remove
print(l1.pop(0))
print(l1)

print("\nlist.remove()")
l1.remove(9)
print(l1)

#Tuples are immutable
print("\nTuples")
t1 = (1,2,2,2,3,4,5,6,7,8,9,"AA")
print(type(t1))
print(t1)
print("\nTuple Methods")

print("\nTuple.count()")
print(t1.count(2))

print("\nTuple.index()")
#returns first occurence of the entered parameter
print(t1.index("AA"))