def remove(list,word):
    n=[]
    for item in list:
        if(item!=word):
            n.append(item.strip(word))
    return n

list=["abc","xyz","ktb","gadp"]
print(remove(list,"abc"))