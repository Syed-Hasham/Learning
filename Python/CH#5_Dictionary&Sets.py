print("\tDictionary & Sets")
#dictionary is collection of keys value pair
#unordered
#indexed
#mutable
#doesn't allow duplicates
print("\n\tDictionary")
D1 ={
    "v1" : 100,
    "v2" : "ABC",
    "v3" : 1.1111,
    4 : True
}
print(D1,type(D1))
print(D1["v2"])
print("\n\tDictionary Methods")
print("\nDictionary.items()\n")
print(D1.items())
print("\nDictionary.keys()\n")
print(D1.keys())
print("\nDictionary.update()\n")
D1.update({"v4":50})
print(D1)
print("\nDictionary.get()\n")
print(D1.get(4))#returns value of specified keys

print("\n\tSets\n")
#No repetition
#Allows Multiple datatypes
#Unordered
#Mutable
#Unindexed
# e = set() #Creates Empty set

S1 = {1,2,3,4,5,6,"ABC"}
S2 = {9,2,6,7}

print(S1,type(S1))
print(S2,type(S2))

print("\n\tSets Methods\n")

print("\nSet.remove\n")
S1.remove("ABC")
print(S1)

print("\nSet.union\n")
print(S1.union(S2))

print("\nSet.intersection\n")
print(S1.intersection(S2))

print("\nSet.pop()\n")
print(S2.pop())

print("\nSet.clear()\n") #empties the set
print(S1.clear())